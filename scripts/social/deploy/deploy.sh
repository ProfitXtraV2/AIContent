#!/bin/sh
# Install a release of the check (tech spec, Host and guest deployment, step 6; boundary 2).
#
#   sudo /opt/px-social/deploy.sh v2026.11.04
#
# Only Nikolay and the setup person can run it (SSH into the guest), and it refuses a tag that one
# of their two SSH keys did not sign: `git verify-tag` against /etc/px-social/allowed_signers
# (one line per person:  <email> namespaces="git" ssh-ed25519 AAAA…). The release holds only
# scripts/; the check's data comes from its own clone of main and is never executed.
set -eu
TAG="${1:-}"
case "$TAG" in
  ""|*[!A-Za-z0-9._-]*) echo "usage: deploy.sh <release tag>"; exit 2 ;;
esac
SRC=/opt/px-social/src                  # a clone used only to fetch and verify tags
REL=/opt/px-social/releases/$TAG
SIGNERS=/etc/px-social/allowed_signers

git -C "$SRC" fetch --tags --force -q origin
if ! git -C "$SRC" -c gpg.format=ssh -c gpg.ssh.allowedSignersFile="$SIGNERS" verify-tag "$TAG"; then
  echo "refused: $TAG is not signed by an allowed key"
  exit 1
fi
if [ ! -d "$REL" ]; then
  rm -rf "$REL.tmp"
  mkdir -p "$REL.tmp"
  git -C "$SRC" archive "$TAG" scripts/ | tar -x -C "$REL.tmp"
  chmod 0755 "$REL.tmp"/scripts/social/deploy/*.sh
  chown -R root:root "$REL.tmp"
  chmod -R go-w "$REL.tmp"
  mv "$REL.tmp" "$REL"
fi
cp "$REL/scripts/social/deploy/backup.sh" /opt/px-social/backup.sh
ln -sfn "$REL" /opt/px-social/current.new
mv -T /opt/px-social/current.new /opt/px-social/current
echo "px-social now runs $TAG"
