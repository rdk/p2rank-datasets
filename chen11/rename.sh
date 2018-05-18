#!/bin/bash

 
for f in *ligand.pdb
do
	newname=`echo $f | sed 's/\_ligand//'`
	echo "$f -> $newname"
	mv $f $newname
done



