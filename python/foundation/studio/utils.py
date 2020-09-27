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

class StudioUtils(object):
    def __init__(self, location=None):
        self._location = location

    def get_foundation_config(self):
        data = None
        with open(self.foundation_config, 'r') as fread:
            data = json.load(fread)

        return data

    @property
    def software_root(self):
        return os.environ['N_SOFTWARE_ROOT']

    @property
    def projects_root(self):
        return os.getenv('N_PROJECT_ROOT', None)

    @property
    def location(self):
        return os.getenv('N_LOCATION', None)

    @property
    def foundation_config(self):
        return os.path.join(os.getenv('REZ_FOUNDATION_ROOT', None), "config/foundation.json")

