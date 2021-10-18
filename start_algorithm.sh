#!/bin/sh

for file in data/*;
do
    python3 "$1" "$file" 
done