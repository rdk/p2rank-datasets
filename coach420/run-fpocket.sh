#!/bin/bash

ls *pdb > list.lst

fplist() {
	mkdir fpocket
	fpocket -F $1 2>&1 | tee fpocket_$1.log
	mv *out *log fpocket
}

fplist list.lst


