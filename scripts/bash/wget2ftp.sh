#!/bin/bash

for filename in contrib filer receipt debt expense; do
      wget --accept $filename.txt -m -qO- ftp://ftp.phila-records.com > net-$filename.txt
  done
