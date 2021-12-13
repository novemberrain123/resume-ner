#!/bin/bash

#this file turns copies all pdfs into the static dir
#and also generates a thumbnail for each pdf

cd static
find . ! -name 'style.css' ! -name 'bg.jpg' -type f -delete
cd ../../data
cp -a deployment/. ../code/static/
cd ../code/static
for file in *.pdf;
do
  if [[ $file =~ ([0-9]+) ]]; then
    NUM=${BASH_REMATCH[1]}
  fi
  filename=$(basename -- "$file")
  gs -o img_$NUM.jpeg -sDEVICE=jpeg -dLastPage=1 $filename
done



