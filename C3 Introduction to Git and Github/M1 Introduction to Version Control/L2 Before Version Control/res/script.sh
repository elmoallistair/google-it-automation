#/usr/bin/bash

# Video: Diffing Files
diff rearrange1.py rearrange2.py
diff validations1.py validations2.py
diff -u validations1.py validations2.py

# Video: Applying Changes
diff -u rearrange1.py rearrange2.py > change.diff
patch cpu_usage.py < cpu_usage.diff

# Video: Practical Application of diff and patch
cp disk_usage.py disk_usage_original.py
cp disk_usage.py disk_usage_fixed.py
diff -u disk_usage_original.py disk_usage_fixed.py > disk_usage.diff
Patch disk_usage.py < disk_usage.diff