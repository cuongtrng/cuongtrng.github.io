#! /bin/bash

./jemdoc index.jemdoc
./jemdoc AY2016.jemdoc

git add -A
git commit -m "add: test"
git push