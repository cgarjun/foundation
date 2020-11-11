# Copyright © 2019 by Arjun Thekkumadathil

# All rights reserved. No part of this publication/code may not be reproduced, 
# distributed, or transmitted in any form or by any means, including 
# photocopying, recording, or other electronic or mechanical methods, 
# without the prior written permission of the publisher/author, except in the 
# case noncommercial uses permitted by copyright law. For permission requests, 
# write to the publisher, addressed “Attention: Nirvana Project,” 
# at the address below.

# email: arjun.thekkumadathil@gmail.com


class Shot(object):
    '''
    '''
    def __init__(self, show, shot, shot_type, frame_range=(1001, 1100), temp_dir=True, config_dir=True):
        self._show = show
        self._shot = shot
        self._shot_type = shot_type
        self._frame_range = frame_range
        self._temp_dir = temp_dir
        self._config_dir = config_dir

    def create(self):
        pass

    @property
    def shot(self):
        return self._shot

    @property
    def shot_type(self):
        return self._shot_type

    @property
    def frame_range(self):
        return self._frame_range