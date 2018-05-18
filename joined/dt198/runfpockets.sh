#!/bin/bash

ls *pdb > list.lst

mkdir fpocket
fpocket -F list.lst 2>&1 | tee run.log
mv *out *log fpocket

