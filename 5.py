#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string

alphabet, i = string.ascii_lowercase, 0
while i < len(alphabet):
    print(alphabet[i:i+5])
    i += 5
