#!/bin/sh

for file in data/*;
do
    python "$1" "$file" 
done