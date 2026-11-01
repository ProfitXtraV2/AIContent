#!/bin/sh
# Nightly backup of the guest (tech spec, Host and guest deployment, step 7), 03:30 UTC:
# the Postiz database, the check's SQLite and Postiz's /uploads, in one archive encrypted with
# `age` to the two people's public keys, copied to the off-host location the setup person named.
# Kept 14 days. The private keys that open it are held offline by the two people.
#
# /etc/px-social/backup.env:  BACKUP_DEST=<rclone remote:path>   POSTIZ_DB_CONTAINER=postiz-postgres
set -eu
. /etc/px-social/backup.env
: "${BACKUP_DEST:?set BACKUP_DEST in /etc/px-social/backup.env}"
DB_CONTAINER="${POSTIZ_DB_CONTAINER:-postiz-postgres}"
UPLOADS="${POSTIZ_UPLOADS:-/var/lib/postiz/uploads}"
stamp=$(date -u +%Y%m%dT%H%M%SZ)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

docker exec "$DB_CONTAINER" sh -c 'pg_dump -U "$POSTGRES_USER" -Fc "$POSTGRES_DB"' > "$work/postiz.dump"
sqlite3 /var/lib/px-social/state.sqlite ".backup '$work/state.sqlite'"
tar -C "$(dirname "$UPLOADS")" -czf "$work/uploads.tar.gz" "$(basename "$UPLOADS")"
tar -C "$work" -cf - postiz.dump state.sqlite uploads.tar.gz \
  | age -R /etc/px-social/age-recipients.txt > "$work/px-social-$stamp.tar.age"
rclone copyto "$work/px-social-$stamp.tar.age" "$BACKUP_DEST/px-social-$stamp.tar.age"
rclone delete --min-age 14d --include 'px-social-*.tar.age' "$BACKUP_DEST"
echo "backup px-social-$stamp.tar.age done"
