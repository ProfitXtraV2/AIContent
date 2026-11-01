#!/bin/sh
# GIT_ASKPASS for the check's data clone: answers git with the GitHub App installation token of
# the current run, which publishing_check.py passes in PX_GIT_TOKEN for that git call only. The
# token is never written to the clone's config or to disk.
case "$1" in
  Username*) echo "x-access-token" ;;
  *) echo "${PX_GIT_TOKEN:?}" ;;
esac
