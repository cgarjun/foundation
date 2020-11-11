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

def get_software_root():
    return os.environ['N_SOFTWARE_ROOT']

def get_projects_root():
    return os.getenv('N_SHOW_ROOT', None)

def get_location():
    return os.getenv('N_LOCATION', None)

def get_foundation_config():
    foundation_config = os.path.join(os.getenv('REZ_FOUNDATION_ROOT', None), "config/foundation.json")
    data = None
    with open(foundation_config, 'r') as fread:
        data = json.load(fread)

    return data

def get_npathx_config():
    """
    docstring
    """
    npathx_config = os.path.join(os.getenv('REZ_FOUNDATION_ROOT', None), "config/npathx.json")
    data = None
    with open(npathx_config, 'r') as fread:
        data = json.load(fread)

    return data