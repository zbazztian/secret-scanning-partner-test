#!/bin/env python3
from random import randint
from itertools import chain

asc = [
  chr(x) for x in \
  chain(
    range(48, 58),
    range(65, 91),
    range(97, 123),
    range(47, 48),
    range(43, 44)
  )
]

#print(asc)
for x in range(50):
  t = ''.join([asc[randint(0, len(asc) - 1)] for x in range(40)])
  print(t)
