#!/bin/bash

i=1
for file in *.txt; do
    mv "$file" "file_$i.txt"
    ((i++))
done

echo "✅ All .txt files renamed!"
