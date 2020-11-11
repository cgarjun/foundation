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
import shutil
import subprocess
from nlogger.logger import logging

class Suite(object):
    '''
    '''
    def __init__(self, suite_root, suite_name):
        self._suite_root= suite_root
        self._suite_name = suite_name

    def create(self):
        '''
            Creates an empty suite
        '''
        logging.info("Creating a new rez-suite names {0}".format(self.suite_name))
        cmd = "rez-suite {0} --create".format(self.suite_dir)
        logging.debug("CMD EXEC: {0}".format(cmd))
        process = subprocess.Popen([cmd], shell=True)
        process.communicate()
        return True

    def release(self):
        '''
            Switches the current to the specified suite
        '''
        dest = os.path.join(self._suite_root, "current")
        if os.path.exists(dest):
            os.remove(dest)
        os.symlink(self.suite_dir, dest)
        logging.info("Releasing {0} to production".format(self._suite_name))
        return True

    def clone(self, source_suite):
        '''
        '''
        raise NotImplementedError
        # if self._validate_source_suite(source_suite):
        #     self.create()
        #     shutil.copytree(source_suite, self.suite_dir)


    def _validate_source_suite(self, source_suite):
        return os.path.isfile(os.path.join(source_suite, 'suite.yaml'))

    @property
    def suite_dir(self):
        return os.path.join(self._suite_root, self._suite_name)

    @property
    def suite_name(self):
        return self._suite_name