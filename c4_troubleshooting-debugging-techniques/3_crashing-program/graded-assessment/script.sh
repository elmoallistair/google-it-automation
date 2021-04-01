#/usr/bin/bash

# ImportError
cd /
python3 /usr/bin/infrastructure
sudo apt install python3-pip
pip3 install matplotlib

# NoFileError
python3 /usr/bin/infrastructure
cd ~
ls
mv data.bak data.csv

# MissingColumnError
cat ~/data.csv
sudo chmod 777 ~/data.csv
nano ~/data.csv
python3 /usr/bin/infrastructure
