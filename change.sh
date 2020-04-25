#!/bin/bash
for system in $(cat ../../../mol_list/DP284_Dip152.list)
do
  	cd $system
        rm *out
        cp ../subtem.pbs subtem.pbs
        sed -i '6s/.*/BASIS                 6-31+g/' mol.in
        qsub subtem.pbs
        cd ..
done
