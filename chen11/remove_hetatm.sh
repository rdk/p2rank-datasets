#!/bin/bash

mkdir clean

for f in *.pdb
do
	newf="clean/$f"
	echo "$f -> $newf"
	cat $f | grep -v "^HETATM" > "$newf"
done