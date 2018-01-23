#!/usr/bin/env bash

alias python=python3.6

mkdir ~/env
python -m venv ~/env/hippo
source ~/env/hippo/bin/activate
mkdir ~/hippo
cd ~/hippo

git init
git remote add origin https://github.com/kandhan-kuhan-t/hippo.git
git config --global credential.helper store
git pull origin master
pip install -r ./req.txt
echo "Starting Report Testing, sending system configuration email..."
~/env/hippo/bin/python ./test_cron.py
nohup ~/env/hippo/bin/python ./cron.py
echo "System report email has been sent, check .mail.log for more details"
echo "Cron job has started, check .cron.log for more details"

