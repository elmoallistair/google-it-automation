#!/bin/bash

> oldFiles.txt

files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)

for f in $files; do
  if [ -e $HOME$f ]; then
  	echo $HOME$f >> oldFiles.txt
  fi
done