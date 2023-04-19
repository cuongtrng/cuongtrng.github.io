#! /bin/bash

./jemdoc index.jemdoc
./jemdoc AY2016.jemdoc

now=$(date) 
git add -A
git commit -m "change on $(now) "
git push