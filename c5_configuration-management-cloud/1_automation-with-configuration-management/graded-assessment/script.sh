#/env/bin/bash

echo $PATH
export PATH=/bin:/usr/bin
cd /etc/puppet/code/environments/production/modules/profile/manifests
sudo nano init.pp
sudo puppet agent -v --test
echo $PATH
