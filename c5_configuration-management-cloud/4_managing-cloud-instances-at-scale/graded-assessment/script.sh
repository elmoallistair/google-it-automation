sudo systemctl status apache2 # failed to start
sudo systemctl restart apache2 # restart
sudo systemctl status apache2 # failed to start, port 80 is being used by the other process,
sudo netstat -nlp # find which processes are listening on which ports
ps -ax | grep python3 # find out which python3 program name that's using port 80
cat /usr/local/bin/jimmytest.py # look at the code
sudo kill [process-id] # kill the process created by /usr/local/bin/jimmytest.py. Replace [process-id] with the PID of the python3 program 
ps -ax | grep python3 # list the processes again to find out if the process we just killed was actually terminated
sudo systemctl --type=service | grep jimmy # check for the availability of any service with the keywords "python" or "jimmy"
sudo systemctl stop jimmytest && sudo systemctl disable jimmytest # stop and disable the service
sudo netstat -nlp # confirm that no processes are listening on 80
sudo systemctl start apache2 # start apache2 again
