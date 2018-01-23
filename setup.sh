#!/usr/bin/env bash

alias python=python3.6

python -m venv ~/env/hippo__
source ~/env/hippo__/bin/activate
mkdir ~/hippo__
cd ~/hippo__
git init
git remote add origin 
pip install -r ./req.txt