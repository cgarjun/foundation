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

    def __init__(self, show=None, entity_type=None, entity_name=None, task=None):
        self._show = show
        self._entity_type = entity_type
        self._entity_name = entity_name
        self._task = task

    @classmethod
    def get_from_env(cls):
        show = None
        entity_type = None
        entity_name = None
        task=None
        show = os.getenv('N_SHOW', None)
        if show:
            show = show

        entity_type = os.getenv('N_ENTITY_TYPE', None)
        if entity_type:
            entity_type = entity_type

        entity_name = os.getenv('N_ENTITY', None)
        if entity_name:
            entity_name = entity_name

        task = os.getenv('N_TASK', None)
        if task:
            task = task
        return cls(show, entity_type, entity_name, task)

    @property
    def show(self):
        return self._show

    @property
    def entity_type(self):
        return self._entity_type

    @property
    def entity_name(self):
        return self._entity_name

    @property
    def task(self):
        return self._task
