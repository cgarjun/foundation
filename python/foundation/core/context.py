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

class Context(object):

    def __init__(self, show=None, sequence=None, shot=None, task=None):
        self._show = show
        self._sequence = sequence
        self._shot = shot
        self._task = task

    @classmethod
    def get_from_env(cls):
        show = None
        sequence = None
        shot = None
        task=None
        show = os.getenv('N_SHOW', None)
        if show:
            show = show

        sequence = os.getenv('N_sequence', None)
        if sequence:
            sequence = sequence

        shot = os.getenv('N_ENTITY', None)
        if shot:
            shot = shot

        task = os.getenv('N_TASK', None)
        if task:
            task = task
        return cls(show, sequence, shot, task)

    def get_shot_type(self):
        """
        docstring
        """
        if self.shot:
            return 'SHOT_TYPE'
        else:
            raise AttributeError('Shot not defined in the Context instance')

    @property
    def show(self):
        return self._show

    @property
    def sequence(self):
        return self._sequence

    @property
    def shot(self):
        return self._shot

    @property
    def task(self):
        return self._task
