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
import subprocess
from foundation.studio.flog import logging
from foundation.studio import config

class Profile(object):
    '''
        Wrapper class around rez-suite to get easy workflow and 
        managing releases as per production needs.
    '''
    def __init__(self, suite_root, suite_name, force=False):
        self._suite_root= suite_root
        self._suite_name = suite_name
        self._config = None
        self.force = force
        self._set_suite_mapper()

    def _set_suite_mapper(self):
        '''
            Sets the config file
        '''
        driverObj = config.DriverJSON()
        package_config = config.Config('foundation', 'suite_mapper', driverObj)
        self._config = package_config.resolve()

    def _generate_rez_rxt(self, profile_name, packages):
        '''
            Generate rxt file to add to the suite
        '''
        output_path = os.path.join(self._suite_root, "{0}.rxt".format(profile_name))
        cmd = "rez-env "
        cmd += " ".join(packages)
        cmd += " --output "
        cmd += output_path
        logging.debug("CMD EXEC: {0}".format(cmd))
        process = subprocess.Popen([cmd], shell=True)
        process.communicate()
        return output_path

    def _add_to_suite(self, profile_name, rxt_file, prefix=None, suffix=None):
        '''
            Add rxt file to the suite
        '''
        logging.info("Adding context to rez suite")
        cmd = "rez-suite --add {0} --context {1} {2}".format(rxt_file, profile_name, self.suite_dir)
        if prefix:
            cmd += " --prefix {0}".format(prefix)

        if suffix:
            cmd += " --suffix {0}".format(suffix)

        logging.debug("CMD EXEC: {0}".format(cmd))
        process = subprocess.Popen([cmd], shell=True)
        process.communicate()

    def _force_profile_patch(self, profile_name):
        '''
            This is not a recommended usage in production this only for debugging,
            this function removes the existing profile from a suite.

            Arguments:
                profile_name: Name of profile in the config to be patched
        '''
        logging.warn("Force Patching existing profile")
        os.chdir(self._suite_root)
        cmd = "rez-suite -r {0} {1}".format(profile_name, self.suite_dir)
        logging.debug("CMD EXEC: {0}".format(cmd))
        process = subprocess.Popen([cmd], shell=True)
        process.communicate()

    def generate_all_profiles(self, force=False):
        '''
            Generates profiles for all the elemets in the config file.

            Keyword Arguments:
                creation: if creation set to true that will create a new empty suite
                force: if force enabled, existing profile will be removed and create a
                       new one
        '''
        for conf in self._config:
            rxt_file = self._generate_rez_rxt(conf, self._config[conf])
            if self.force:
                self._force_profile_patch(conf)
            self._add_to_suite(conf, rxt_file)
            # os.remove(rxt_file)
        return True

    def generate_profile(self, profile_name, force=False):
        '''
            Creates and add profile to

            Arguments:
                profile_name: Name of profile in the config to be patched
        '''
        if self.force:
            self._force_profile_patch(profile_name)
        logging.info("Generating new profile {0}".format(profile_name))
        rxt_file = self._generate_rez_rxt(profile_name, self._config[profile_name]['packages'])
        self._add_to_suite(profile_name, rxt_file, self._config[profile_name]['prefix'], self._config[profile_name]['suffix'])
        os.remove(rxt_file)    

    @property
    def suite_dir(self):
        return os.path.join(self._suite_root, self._suite_name)
