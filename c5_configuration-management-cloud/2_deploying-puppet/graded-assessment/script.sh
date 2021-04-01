# Install packages
cd /etc/puppet/code/environments/production/modules/packages
sudo chmod 646 manifests/init.pp
nano manifests/init.pp
gcloud compute instances describe linux-instance --zone=us-central1-a --format='get(networkInterfaces[0].accessConfigs[0].natIP)' # outputs external IP address

## new terminal
ssh -i <XXXXX.pem> <username>@<external Ip Address>
## linux-instance VM instance terminal
sudo puppet agent -v --test
apt policy golang

# Fetch machine information
## Puppet VM terminal
cd /etc/puppet/code/environments/production/modules/machine_info
sudo chmod 646 manifests/init.pp
nano manifests/init.pp

# Puppet Templates
sudo chmod 646 templates/info.erb
## linux-instance VM terminal
sudo puppet agent -v --test
cat /tmp/machine_info.txt

## Reboot machine
sudo mkdir -p /etc/puppet/code/environments/production/modules/reboot/manifests
cd /etc/puppet/code/environments/production/modules/reboot/manifests
sudo nano init.pp
sudo nano /etc/puppet/code/environments/production/manifests/site.pp 
sudo puppet agent -v --test
