#!/usr/bin/env bash

SECONDS=0
OS_TARGET_PATH=".."
OS_TARGET_NAME=osdna-meteor-frontend-$(date +%Y-%m-%d-%s).tar.gz

meteor build $OS_TARGET_PATH/ --architecture=os.linux.x86_64
mv $OS_TARGET_PATH/osdna-meteor-frontend.tar.gz $OS_TARGET_PATH/$OS_TARGET_NAME

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
