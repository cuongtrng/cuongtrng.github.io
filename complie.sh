#! /bin/bash

dir=$(pwd)
shopt -s extglob

cd jemdoc_files
./jemdoc -o ../ *.jemdoc
cd $dir

# php -S localhost:8000