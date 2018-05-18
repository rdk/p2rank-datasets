#!/bin/bash

#ls *pdb > list.lst

fplist() {
	mkdir fpocket
	fpocket -F $1 2>&1 | tee run_$1.log
	mv *out *log fpocket	
}

fplist list1.lst 
fplist list2.lst 
fplist list3.lst 
fplist list4.lst 
fplist list5.lst 


