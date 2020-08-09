vim tools.pp
htop # check that the command isn't present yet
sudo puppet apply -v tools.pp # running rules
sudo puppet apply -v ntp.pp # running rules
sudo puppet apply -v webserver.pp # running rules
