#! /bin/bash

dir=$(pwd)
shopt -s extglob

python3 gen_conf.py 

cd jemdoc_files
./jemdoc -o ../ *.jemdoc
cd $dir

# php -S localhost:8000