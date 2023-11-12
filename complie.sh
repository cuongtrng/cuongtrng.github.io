#! /bin/bash

dir=$(pwd)
shopt -s extglob

cd jemdoc_files
./jemdoc -c mysite.conf -o ../ *.jemdoc
cd $dir

# php -S localhost:8000