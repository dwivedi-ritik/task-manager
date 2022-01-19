#!/bin/bash

pip install -r requirements.txt
python create_table.py


curr_dir=$(pwd)

echo "Making task.py as executable"

default_shell=$(echo $SHELL | awk '{split($0,a, "/"); print a[4]}')

chmod +x task

echo "Adding current directory in path of your bashrc"

echo "export PATH=${curr_dir}" >> ~/.${default_shell}rc

echo "Do not delete this directory"