#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string

token = '_'+''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))

print(token)
