#!/bin/bash
###############################################################################
# Copyright (c) 2017-2018 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################

set -e

if [ -f $APP_SOURCE_DIR/launchpad.conf ]; then
  source <(grep INSTALL_GRAPHICSMAGICK $APP_SOURCE_DIR/launchpad.conf)
fi

if [ "$INSTALL_GRAPHICSMAGICK" = true ]; then
  printf "\n[-] Installing Graphicsmagick...\n\n"

  apt-get update
  apt-get install -y graphicsmagick graphicsmagick-imagemagick-compat 
fi