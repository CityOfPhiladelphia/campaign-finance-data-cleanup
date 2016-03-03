#/bin/bash

find . -name filer.txt | while read line; do
  cat "$line" >> net-filer.txt
  echo >> net-filer.txt
  echo 'script complete'
done


