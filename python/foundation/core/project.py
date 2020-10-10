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
import json
import shutil
from foundation.studio.nlog import logging
from foundation.studio import utils, config

class ProjectConfig:
    def __init__(self, **config_data):
        for k,v in config_data.items():
            if isinstance(v,dict):
                self.__dict__[k] = ProjectConfig(**v)
            else:
                self.__dict__[k] = v


def get_show_spec(config_file=None):
    """
    docstring
    """
    project_config = json.load(open(config_file))
    return ProjectConfig(**project_config)

def get_template(template_name):
    """
    docstring
    """
    return os.path.join(os.getenv('N_SHOW_TEMPLATE_DIR', None), template_name)


class ProjectEntity(object):
    def __init__(self, config_file, template_name):
        """
        docstring
        """
        self._config_file = config_file
        self._template_name = template_name
        
        self._project_name = None
        self._project_path = None

        self.initialize()

    def initialize(self):
        """
        docstring
        """
        show_spec = get_show_spec(self.config_file)
        self.project_name = show_spec.name
        projects_root_path = utils.get_projects_root()
        self.project_path = os.path.join(projects_root_path, self.project_name)

    def install_show_spec(self):
        """
        docstring
        """
        logging.info("Installing showspec...")
        destination_config = os.path.join(self.project_path, 'config/showspec.json')
        print destination_config
        # shutil.copy(self.config_file, )


    def create(self):
        """
        docstring
        """
        logging.info("Creating show on disk...")
        source_template = get_template(self.template_name)
        logging.info("Source template: {0}".format(source_template))
        logging.info("Destination template: {0}".format(self.project_path))
        shutil.copytree(source_template, self.project_path)
        self.install_show_spec()

    @property
    def config_file(self):
        """
        docstring
        """
        return self._config_file

    @property
    def template_name(self):
        """
        docstring
        """
        return self._template_name

    @property
    def project_name(self):
        """
        docstring
        """
        return self._project_name
    
    @project_name.setter
    def project_name(self, value):
        """
        docstring
        """
        self._project_name = value

    @property
    def project_path(self):
        """
        docstring
        """
        return self._project_path

    @project_path.setter
    def project_path(self, value):
        """
        docstring
        """
        self._project_path = value

