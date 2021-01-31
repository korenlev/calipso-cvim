###############################################################################
# Copyright (c) 2017-2020 Koren Lev (Cisco Systems),                          #
# Yaron Yogev (Cisco Systems), Ilia Abashin (Cisco Systems) and others        #
#                                                                             #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Apache License, Version 2.0       #
# which accompanies this distribution, and is available at                    #
# http://www.apache.org/licenses/LICENSE-2.0                                  #
###############################################################################
from scan.processors.processor import Processor


class ProcessRegionsMetros(Processor):
    PREREQUISITES = []
    COLLECTION = "environments_config"

    def run(self):
        super().run()

        env_doc = self.inv.find_one({"name": self.env}, collection=self.COLLECTION)
        cvim_region = env_doc.get('cvim_region')
        cvim_metro = env_doc.get('cvim_metro')
        if not cvim_region and not cvim_metro:
            return

        docs = self.inv.find_items({"environment": self.env})

        for doc in docs:
            doc['cvim_region'] = cvim_region
            doc['cvim_metro'] = cvim_metro
            self.inv.set(doc)
