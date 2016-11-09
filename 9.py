#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string

alphabet, i = string.ascii_lowercase, 0
symbol = input('Enter symbol: ')
i = alphabet.find(symbol)

if(symbol == 'z'):
	print(alphabet[:3])
elif(symbol == alphabet[-2]):
	print(alphabet[-1], alphabet[:2])
elif(symbol == alphabet[-3]):
	print(alphabet[-2], alphabet[-1], alphabet[0])
else:
	print(alphabet[i+1:i+4])
