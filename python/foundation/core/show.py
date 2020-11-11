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
from nlogger.logger import logging
from foundation.studio import utils, config
from foundation.utils import datautils

def get_template(template_name):
    """
    docstring
    """
    return os.path.join(os.getenv('N_SHOW_TEMPLATE_DIR', None), template_name)


class Show(object):
    def __init__(self, show_name, template_name):
        """
        docstring
        """
        self._template_name = template_name
        
        self._show_name = show_name
        self._show_path = None

        self.initialize()

    def initialize(self):
        """
        docstring
        """
        projects_root_path = utils.get_projects_root()
        self.project_path = os.path.join(projects_root_path, self.show_name)

    def create(self):
        """
        docstring
        """
        logging.info("Creating show on disk...")
        source_template = get_template(self.template_name)
        logging.info("Source template: {0}".format(source_template))
        logging.info("Destination template: {0}".format(self.project_path))
        shutil.copytree(source_template, self.project_path)

    @property
    def template_name(self):
        """
        docstring
        """
        return self._template_name

    @property
    def project_path(self):
        """
        docstring
        """
        return self._show_path

    @project_path.setter
    def project_path(self, value):
        """
        docstring
        """
        self._show_path = value

    @property
    def show_name(self):
        """
        docstring
        """
        return self._show_name

