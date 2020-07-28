#!/usr/bin/env python3

import sys
import subprocess

file = sys.argv[1]
with open(file) as f:
  for line in f.readlines():
      source = line.strip()
      destination = source.replace('jane', 'jdoe')
      subprocess.run(['mv', source, destination])
  f.close()