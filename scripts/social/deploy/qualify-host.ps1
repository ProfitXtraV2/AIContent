#Requires -RunAsAdministrator
<#
  S0: qualify the Windows host for the social guest (tech spec, "Host and guest deployment",
  step 0). Run it elevated on the host and paste the output into SOCIAL-SETUP.md under
  "Host qualification". It only reads; it changes nothing. Groups are found by their well-known
  SIDs, so a Windows in any language gives the same answer.

  Needs: Windows with Hyper-V (Pro, Enterprise or Server; Home does not qualify), at least
  4 vCPU, 8 GB RAM and 80 GB of disk free beyond current use, no sleep, updates outside
  09:00-20:00, BitLocker on the guest's disk, and administrators limited to the two people.
#>
$ErrorActionPreference = 'Continue'

function Show($label, $value) { '{0,-40} {1}' -f $label, $value }

function PowerAc($setting) {
    # powercfg prints min, max, step, then the AC and DC values (in hex); the labels are localised
    try {
        $hex = powercfg /query SCHEME_CURRENT SUB_SLEEP $setting | Select-String '0x[0-9a-fA-F]{8}' -AllMatches |
            ForEach-Object { $_.Matches } | ForEach-Object { $_.Value }
        [Convert]::ToInt64($hex[-2], 16)
    } catch { 'unknown' }
}

function Members($sid) {
    try {
        $group = Get-LocalGroup -SID $sid -ErrorAction Stop
        $list = Get-LocalGroupMember -Group $group -ErrorAction Stop | ForEach-Object { "$($_.Name) ($($_.ObjectClass))" }
        if ($list) { "$($group.Name): " + ($list -join '; ') } else { "$($group.Name): (none)" }
    } catch { "group $sid not present" }
}

"## Host qualification - $(Get-Date -Format 'yyyy-MM-dd HH:mm') - $env:COMPUTERNAME"
''
'```'
'--- Windows and Hyper-V'
$os = Get-CimInstance Win32_OperatingSystem
$cs = Get-CimInstance Win32_ComputerSystem
$cpu = Get-CimInstance Win32_Processor | Select-Object -First 1
Show 'Edition' $os.Caption
Show 'Version / build' "$($os.Version) / $($os.BuildNumber)"
try {
    $hv = Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -ErrorAction Stop
    Show 'Hyper-V feature' $hv.State
} catch { Show 'Hyper-V feature' 'not available (Windows Home does not qualify)' }
Show 'Firmware virtualisation' $cpu.VirtualizationFirmwareEnabled
Show 'Hypervisor running' $cs.HypervisorPresent
Show 'Host model (VM if virtual)' "$($cs.Manufacturer) $($cs.Model)"

'--- Resources'
Show 'Logical processors' $cs.NumberOfLogicalProcessors
Show 'RAM total (GB)' ([math]::Round($cs.TotalPhysicalMemory / 1GB, 1))
Show 'RAM free now (GB)' ([math]::Round($os.FreePhysicalMemory * 1KB / 1GB, 1))
Get-CimInstance Win32_LogicalDisk -Filter 'DriveType=3' | ForEach-Object {
    Show "Disk $($_.DeviceID) free / size (GB)" ("{0} / {1}" -f [math]::Round($_.FreeSpace / 1GB, 1), [math]::Round($_.Size / 1GB, 1))
}
try {
    $vms = Get-VM -ErrorAction Stop
    Show 'Existing VMs' (($vms | ForEach-Object { "$($_.Name) [$($_.State), $([math]::Round($_.MemoryAssigned / 1GB, 1)) GB]" }) -join '; ')
} catch { Show 'Existing VMs' '(Hyper-V tools not installed)' }

'--- Power and updates'
powercfg /a
Show 'Sleep after (AC, seconds; 0 = never)' (PowerAc 'STANDBYIDLE')
Show 'Hibernate after (AC, seconds; 0 = never)' (PowerAc 'HIBERNATEIDLE')
$ux = Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings' -ErrorAction SilentlyContinue
Show 'Update active hours (want 9-20)' "$($ux.ActiveHoursStart) - $($ux.ActiveHoursEnd)"

'--- Disk encryption'
try {
    Get-BitLockerVolume -ErrorAction Stop | ForEach-Object {
        Show "BitLocker $($_.MountPoint)" "$($_.VolumeStatus), protection $($_.ProtectionStatus), keys: $(($_.KeyProtector | ForEach-Object KeyProtectorType) -join ', ')"
    }
} catch { Show 'BitLocker' 'not available on this edition' }

'--- Everyone with administrator rights or remote access'
Members 'S-1-5-32-544'      # Administrators
Members 'S-1-5-32-578'      # Hyper-V Administrators
Members 'S-1-5-32-555'      # Remote Desktop Users
Members 'S-1-5-32-580'      # Remote Management Users
$rdp = Get-ItemProperty 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -ErrorAction SilentlyContinue
Show 'Remote Desktop enabled' ($rdp.fDenyTSConnections -eq 0)
Show 'WinRM service' ((Get-Service WinRM -ErrorAction SilentlyContinue).Status)
$tools = 'TeamViewer|AnyDesk|RustDesk|Chrome Remote Desktop|Splashtop|ScreenConnect|ConnectWise|LogMeIn|GoTo|Parsec|RealVNC|TightVNC|UltraVNC|NoMachine|Radmin|Zoho Assist|Supremo|Ammyy'
$apps = Get-ItemProperty 'HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*', 'HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*' -ErrorAction SilentlyContinue |
    Where-Object { $_.DisplayName -match $tools } | ForEach-Object { $_.DisplayName }
Show 'Remote-support apps installed' ($(if ($apps) { ($apps | Sort-Object -Unique) -join '; ' } else { '(none found)' }))
Show 'Cloudflare tunnels already here' ((Get-Process cloudflared -ErrorAction SilentlyContinue | Measure-Object).Count)
'```'
''
'Record also, by hand: who holds the BitLocker recovery keys, and who has physical access.'
