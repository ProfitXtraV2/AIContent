#Requires -RunAsAdministrator
<#
  The monthly host audit (tech spec, "Host and guest deployment", step 9): the host's
  administrator groups, remote-access users and tools, and BitLocker. Run it elevated on the
  host and append the output to SOCIAL-SETUP.md under "Monthly host audits". Any account
  beyond Nikolay's and the setup person's is removed, and the guest's secrets are replaced as in
  S0. It only reads; it changes nothing.
#>
$ErrorActionPreference = 'Continue'

function Members($sid) {
    try {
        $group = Get-LocalGroup -SID $sid -ErrorAction Stop
        $list = Get-LocalGroupMember -Group $group -ErrorAction Stop | ForEach-Object { $_.Name }
        '{0,-28} {1}' -f $group.Name, $(if ($list) { $list -join '; ' } else { '(none)' })
    } catch { "group $sid not present" }
}

"### Host audit - $(Get-Date -Format 'yyyy-MM-dd') - $env:COMPUTERNAME"
''
'```'
Members 'S-1-5-32-544'      # Administrators
Members 'S-1-5-32-578'      # Hyper-V Administrators
Members 'S-1-5-32-555'      # Remote Desktop Users
Members 'S-1-5-32-580'      # Remote Management Users
$rdp = Get-ItemProperty 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -ErrorAction SilentlyContinue
'{0,-28} {1}' -f 'Remote Desktop enabled', ($rdp.fDenyTSConnections -eq 0)
$tools = 'TeamViewer|AnyDesk|RustDesk|Chrome Remote Desktop|Splashtop|ScreenConnect|ConnectWise|LogMeIn|GoTo|Parsec|RealVNC|TightVNC|UltraVNC|NoMachine|Radmin|Zoho Assist|Supremo|Ammyy'
$apps = Get-ItemProperty 'HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*', 'HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*' -ErrorAction SilentlyContinue |
    Where-Object { $_.DisplayName -match $tools } | ForEach-Object { $_.DisplayName }
'{0,-28} {1}' -f 'Remote-support apps', $(if ($apps) { ($apps | Sort-Object -Unique) -join '; ' } else { '(none found)' })
try {
    Get-BitLockerVolume -ErrorAction Stop | ForEach-Object {
        '{0,-28} {1}, protection {2}' -f "BitLocker $($_.MountPoint)", $_.VolumeStatus, $_.ProtectionStatus
    }
} catch { 'BitLocker                    not available on this edition' }
try {
    Get-VM -ErrorAction Stop | ForEach-Object { '{0,-28} {1}, start: {2}' -f "VM $($_.Name)", $_.State, $_.AutomaticStartAction }
} catch { }
'```'
