#!/usr/bin/env python3

from multiprocessing import Pool
import multiprocessing
import subprocess
import os

home_path = os.path.expanduser('~')
src = home_path + "/data/prod/"
dest = home_path + "/data/prod_backup/"

if __name__ == "__main__":
    pool = Pool(multiprocessing.cpu_count())
    pool.apply(subprocess.call, args=(["rsync", "-arq", src, dest],))