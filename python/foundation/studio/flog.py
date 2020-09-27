# Copyright © 2019 by Arjun Thekkumadathil

# All rights reserved. No part of this publication/code may not be reproduced, 
# distributed, or transmitted in any form or by any means, including 
# photocopying, recording, or other electronic or mechanical methods, 
# without the prior written permission of the publisher/author, except in the 
# case noncommercial uses permitted by copyright law. For permission requests, 
# write to the publisher, addressed “Attention: Nirvana Project,” 
# at the address below.

# email: arjun.thekkumadathil@gmail.com

import logging
import os

FORMAT = '%(asctime)-15s %(levelname)s %(filename)s %(funcName)s: %(message)s'

logging.basicConfig(level=logging.INFO, format=FORMAT)

if os.environ['DEBUG'] == 1:
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)