#! /bin/bash

dir=$(pwd)

cd main
../jemdoc -c mysite.conf -o ../ index.jemdoc
cd $dir

# now=$(date) 
# git add -A
# git commit -m "change on $(now) "
# git push