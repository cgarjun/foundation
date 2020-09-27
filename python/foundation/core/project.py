# Copyright © 2019 by Arjun Thekkumadathil

# All rights reserved. No part of this publication/code may not be reproduced, 
# distributed, or transmitted in any form or by any means, including 
# photocopying, recording, or other electronic or mechanical methods, 
# without the prior written permission of the publisher/author, except in the 
# case noncommercial uses permitted by copyright law. For permission requests, 
# write to the publisher, addressed “Attention: Nirvana Project,” 
# at the address below.

# email: arjun.thekkumadathil@gmail.com

import os
from foundation.studio.flog import logging
from foundation.studio import utils, config

studio_util = utils.StudioUtils()

class Project(object):
    def __init__(self, project_name, config_file, premissions, update_config):
        self._project_name = project_name
        self._config_file = config_file
        self._premissions = premissions
        self._config = None
        self._update_config = update_config

        self.initialize()

    def initialize(self):
        if self.config_file is None:
            driverObj = config.DriverJSON()
            config_obj= config.Config('foundation', 'projects/{0}'.format(self.project_name), driverObj)
            self.config = config_obj.resolve()
        else:
            raise NotImplementedError("Custom config failed")

    def create_project(self):
        if self.config['project']['short_name'] == self.project_name:
            projects_root = studio_util.projects_root
            project_root = os.path.join(projects_root, self.project_name)
            try:
                os.makedirs(project_root)
            except OSError:
                logging.error("Project {0} already exists".format(self.project_name))
            return project_root
        else:
            raise KeyError("Project name doesn't match to short name in config")

    def create_prod_entities(self, project_root):
        entities = self.config['project']['production_entities']
        for entity in entities:
            entity_root = os.path.join(project_root, entity)
            try:
                os.makedirs(entity_root)
            except OSError:
                logging.error("Project entity {0} already exists".format(entity_root))

    def create_client_entities(self):
        pass

    def create(self):
        project_root = self.create_project()
        self.create_prod_entities(project_root)

    def install_metadata(self, force=False):
        pass

    @property
    def project_name(self):
        return self._project_name

    @property
    def config_file(self):
        return self._config_file

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value

