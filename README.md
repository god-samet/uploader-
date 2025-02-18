# uploader-
remove the limitation of asymmetric ratio for uploading and downloading Iranian servers



 #installation
 ubuntu +20 (python +3.8)

- 1\) you need to install pip, redis & git:

sudo apt install python3-pip python3-venv redis git -y

- Note: Sometimes Redis does not start automatically, start it with the following command

sudo systemctl start redis.service

- 2\) you need to create a directory to clone the project:

mkdir -p /var/www/samet && cd /var/www/samet

- 3\) Clone the project with Git:

git init

git remote add origin 

git pull origin master

- 4\) make virtual environment:

python3 -m venv /var/www/samet/venv

- 5\) Install the project requirements:

cd /var/www/samet && source /var/www/samet/venv/bin/activate && pip install wheel && pip install samet_core/ samet_menu/ && deactivate

- 6\) Create service :

ln -s /var/www/samet/else/samet.service /etc/systemd/system/

- 7\) Reload the service files to include the new service and start :

sudo systemctl daemon-reload && sudo systemctl enable samet.service && sudo systemctl start samet.service

- 8\) Create uploader command to execute menu.py

```bash
ln -s /var/www/samet/else/samet /usr/local/bin/ && chmod +x /usr/local/bin/samet
