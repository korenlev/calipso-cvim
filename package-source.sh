#!/usr/bin/env bash

OS_TARGET_PATH=".."

# Compress current source to a tar object. 
# -exclude: Excluding specific folders and files
# -z: use gzip
# -c: create new archive
# -v: verbose log file processed
# -f: use archive file as target to build the tar to.
tar \
  --exclude='./.meteor/local' \
  --exclude='./node_modules' \
  --exclude='./.git' \
  -zcvf $OS_TARGET_PATH/calipso-source-$(date +%Y-%m-%d-%s).tar.gz .
