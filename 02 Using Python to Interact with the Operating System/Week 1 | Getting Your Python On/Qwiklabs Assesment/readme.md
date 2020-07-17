## Working with Python Scripts

<hr>

### Introduction

In this lab, you'll first have to fix an incorrect Python script. 

### What you’ll do

* Fixing the file permissions to make it executable.
* Fixing a bug in the code

You will have 90 minutes to complete this lab

<hr>

### Accessing the virtual machine

Option 2: OSX and Linux users: Connecting to your VM via SSH

```
chmod 600 ~/Downloads/qwikLABS-XXXXX.pem
ssh -i ~/Downloads/qwikLABS-XXXXX.pem username@External Ip Address
```

### Fix file permissions

```
cd scripts
ls
cat heath_checks.py
./health_checks.py # Expected output: Permission Denied
sudo chmod +x health_checks.py
./health_checks.py # Expected output: "ERROR!"
```

### Debug the issue

```
nano health_checks.py
./health_checks.py # Expected output: "Everything ok"
```

**`health_checks.py`**
```
#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75

# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything ok")
```

### Create a new Python module

```
sudo apt install python3-requests
cd ~/scripts
nano network.py
```

**`network.py`**
```
#!/usr/bin/env python3

import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

def check_connectivity():
    request = requests.get("http://www.google.com")
    return 200
```

### Use the Python module

```
nano health_checks.py
./health_checks.py # Expected output: "Everything ok"
```

**`health_checks.py`**
```
#!/usr/bin/env python3
import shutil
import psutil
from network import *

def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75

# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything ok")
```




