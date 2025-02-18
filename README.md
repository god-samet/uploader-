# uploader-
remove the limitation of asymmetric ratio for uploading and downloading Iranian servers



 #installation
 ubuntu +20 (python +3.8)

- 1\) you need to install pip, redis & git:

```bash
sudo apt install python3-pip python3-venv redis git -y

```

```bash
sudo systemctl start redis.service

```

- 2\) you need to create a directory to clone the project:

```bash
mkdir -p /var/www/samet && cd /var/www/samet

```

- 3\) Clone the project with Git:

```bash
git init
```

```bash
git remote add origin https://github.com/god-samet/uploader-.git
```

```bash
git pull origin master
```

- 4\) make virtual environment:

```bash
python3 -m venv /var/www/samet/venv
```

- 5\) Install the project requirements :

```bash
cd /var/www/samet && source /var/www/samet/venv/bin/activate && pip install wheel && pip install samet_core/ samet_menu/ && deactivate
```

- 6\) Create service :

```bash
ln -s /var/www/samet/else/samet.service /etc/systemd/system/
```

- 7\) Reload the service files to include the new service  :

```bash
sudo systemctl daemon-reload && sudo systemctl enable samet.service && sudo systemctl start samet.service
```

- 8\) Create **uploader** 

```bash
ln -s /var/www/samet/else/samet /usr/local/bin/ && chmod +x /usr/local/bin/samet```
```
