# Copyright © 2019 by Arjun Thekkumadathil

# All rights reserved. No part of this publication/code may not be reproduced, 
# distributed, or transmitted in any form or by any means, including 
# photocopying, recording, or other electronic or mechanical methods, 
# without the prior written permission of the publisher/author, except in the 
# case noncommercial uses permitted by copyright law. For permission requests, 
# write to the publisher, addressed “Attention: Nirvana Project,” 
# at the address below.

# email: arjun.thekkumadathil@gmail.com


import os, json
from abc import ABCMeta, abstractmethod, abstractproperty
from foundation.studio import utils

studio_util = utils.StudioUtils()

class IDriver(object):
    '''
        Interface class for file drivers like json / yaml / txt formats
    '''
    __metaclass__ = ABCMeta
    @abstractmethod
    def load(self, filepath):
        return

    @abstractmethod
    def configuration(self, filepaths):
        return

    @abstractproperty
    def extension(self):
        return

class DriverJSON(IDriver):
    '''
    '''
    def load(self, filepath):
        config = None
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                config = json.load(f)
        else:
            raise IOError("File {0} does not exist".format(filepath))
            
        return config

    def configuration(self, filepaths):
        all_data = {}
        for config_file in filepaths:
            data = self.load(config_file)
            all_data.update(data)
        return all_data

    @property
    def extension(self):
        return 'json'


class Config(object):
    '''
    '''
    def __init__(self, package_name, config_name, driver):
        '''
        '''
        self._package_name = package_name
        self._config_name = config_name
        self._driver = driver

    def _config_from_package(self):
        '''
        '''
        package_root_name = 'REZ_{0}_ROOT'.format(self.package_name.upper())
        package_root = os.getenv(package_root_name, None)
        c_file = os.path.join(package_root, "config/{0}.{1}".format(self.config_name, self.driver.extension))
        if os.path.exists(c_file):
            return c_file
        else:
            raise IOError("Package config file missing")

    def get_all_config_files(self):
        '''
        '''
        config_files = [self._config_from_package()]
        config_hirearchy = studio_util.get_foundation_config()["config_hierarchy"]
        for i in config_hirearchy:
            base_path = os.path.expandvars(i)
            cfile = os.path.join(base_path, self.package_name, self.config_name, self.driver.extension)
            if os.path.exists(cfile):
                config_files.append(cfile)
        return config_files

    def resolve(self):
        '''
        '''
        c_files = self.get_all_config_files()
        data = self.driver.configuration(c_files)

        return data

    @property
    def package_name(self):
        return self._package_name

    @property
    def config_name(self):
        return self._config_name

    @property
    def driver(self):
        return self._driver