# Fetching supplier data
sudo chmod +x ~/download_drive_file.sh
./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz
tar xf ~/supplier-data.tar.gz

# Working with supplier images
nano ~/changeImage.py # script to process the supplier images
sudo chmod +x ~/changeImage.py
./changeImage.py
file ~/supplier-data/images/003.jpeg # check image specifications

# Uploading images to web server
nano ~/supplier_image_upload.py # complete the script with the same technique as used in the file example_upload.py
sudo chmod +x ~/supplier_image_upload.py
./supplier_image_upload.py

# Uploading the descriptions
nano ~/run.py # write a python script named run.py to process the text files
sudo chmod +x ~/run.py
./run.py

# Generate a PDF report and send it through email
nano ~/reports.py # ceate a script reports.py to generate PDF report to supplie
nano ~/emails.py 
nano ~/report_email.py
sudo chmod +x ~/report_email.py
./report_email.py

# Health check
nano ~/health_check.py # write a Python script that will run in the background monitoring some of your system statistics
sudo chmod +x ~/health_check.py
./health_check.py
sudo apt install stress # install the stress tool to test script
stress --cpu 8 # call the tool using a good number of CPUs to fully load our CPU resources
./health_check.py
crontab -e # setting a cron job that executes the script health_check.py every 60 seconds and sends health status to the respective user
