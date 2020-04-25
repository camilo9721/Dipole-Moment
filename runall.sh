#!/bin/sh
for i in $(ls *.out)
do
  	python3 proc.py $i
done
rm *out
