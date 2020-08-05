#!/usr/bin/env python3
# Code from Coursera

import csv
import os
import matplotlib
import numpy as np

class NoFileError(Exception):
  pass

class MissingColumnError(Exception):
  pass

columns = {'firstname','surname','company','job title'}

try:
  CSV_FILE = os.path.expanduser('~') + '/data.csv'

  if not os.path.isfile(CSV_FILE):
    print('Scanning for data.csv...')
    raise NoFileError
  else:
    with open(CSV_FILE) as f:
      csv_data = np.genfromtxt(f,delimiter=',',dtype=str)
      missing_column = list(columns - set(csv_data[0]))
      
      if missing_column:
        raise MissingColumnError
      f.close()

except NoFileError:
  print("NoFileError: Could not find data.csv in the working directory")

except MissingColumnError:
  print("MissingColumnError: Could not find column {} in data.csv".format(missing_column[0]))
