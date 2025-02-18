#!/usr/bin/env bash

echo 'Install prerequisites (step 1)'
apt update && apt install python3-pip python3-venv redis git -y
if [ $? == 0 ]; then
  echo 'Successfully installed'
else
  echo 'An error occurred while installing the prerequisites'
  exit
fi

echo 'start redis service'
systemctl start redis.service
if [ $? == 0 ]; then
  echo 'redis service started'
else
  echo 'service starting failed'
  exit
fi

echo "Creating samet directory (step 2)"
mkdir -p /var/www/samet && cd /var/www/samet

echo 'Pulling the repository (step 3)'
git init
git remote add origin https://github.com/malkemit/namizun.git
git pull origin master
if [ $? != 0 ]; then
  echo 'could not clone the repository'
  exit
fi

echo 'Create virtual env (step 4)'
python3 -m venv /var/www/samet/venv
if [ $? != 0 ]; then
  echo "VENV didn't created"
fi

echo 'Installing project dependencies (step 5)'
cd /var/www/samet && source /var/www/samet/venv/bin/activate && pip install wheel && pip install samet_core/ samet_menu/ && deactivate
if [ $? != 0 ]; then
  echo "Dependencies doesn't installed correctly"
  exit
fi

echo 'Create samet service (step 6)'
ln -s /var/www/samet/else/samet.service /etc/systemd/system/
if [ $? != 0 ]; then
  echo 'Creating service was failed'
  exit
fi

echo 'Reload services and start samet.service (step 7)'
systemctl daemon-reload
sudo systemctl enable samet.service
sudo systemctl start samet.service
if [ $? != 0 ]; then
  echo "Samet service didn't started"
  exit
fi

echo "make samet as a command (step 8)"
ln -s /var/www/samet/else/samet /usr/local/bin/ && chmod +x /usr/local/bin/samet
if [ $? != 0 ]; then
  echo "failed to add samet to PATH environment variables"
  exit
fi