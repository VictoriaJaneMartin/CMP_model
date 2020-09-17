#!/bin/bash

# nb: $1 starts counting from 0
nstart=1
index=$1
echo $index
let index=$(echo $index+$nstart | bc -l)

# input and output directory
script_dir="/afs/cern.ch/user/l/lprincip/public/workingDM/simReco/runs/1000evt_batch"
file_dir="/afs/cern.ch/user/l/lprincip/public/workingDM/simReco/runs/1000evt_batch/output/20200312_100evt_$index"

# standard asetup on condor 
export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh
# set up release you want
asetup 21.0.108,Athena,here

# fetch run script
cp ${script_dir}/39_5050_reco.sh run.sh
chmod +x run.sh

# fetch input HITS file
cp ${file_dir}/HITS.pool.root .

./run.sh

ls -l >> ls.txt
rm -f HITS.pool.root

# copy your output to eg eos
cp *.pool.root ${file_dir}
cp log.* ${file_dir}
cp ls.txt ${file_dir}
cp tmp.RDO ${file_dir}
