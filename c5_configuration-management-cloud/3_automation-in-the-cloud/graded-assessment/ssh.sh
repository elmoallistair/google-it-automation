git clone https://www.github.com/google/it-cert-automation-practice.git
cd ~/it-cert-automation-practice/Course5/Lab3
sudo cp hello_cloud.py /usr/local/bin/
sudo cp hello_cloud.service /etc/systemd/system
sudo systemctl enable hello_cloud.service