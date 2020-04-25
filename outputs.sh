#!/bin/sh
for system in $(cat ../../../mol_list/DP284_Dip152.list)
do
  	cd $system
        cp mol.out $system.out
        mv $system.out ../../../Results
        cd ..
done
