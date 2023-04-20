#!/bin/bash

for dir in $1/* ;
do
    python3 /home/fuchs/aglippert/machajewskim/csvdata/simplepars.py $dir
done; 
