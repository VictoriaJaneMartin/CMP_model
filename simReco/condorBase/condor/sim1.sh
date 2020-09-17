#!/bin/bash

# nb: $1 starts counting from 0
nstart=1
index=$1
nskip=$(echo $index*100 | bc -l)
let index=$(echo $index+$nstart | bc -l)

# input and output directory
script_dir="$WORK/private/workingDM/simReco/runs/1000evt_batch"
file_dir="$WORK/private/workingDM/simReco/runs/1000evt_batch/output/20200312_100evt_$index"
evnt_dir="$WORK/private/workingDM/gen/20200304run01"
# standard asetup on condor 
export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh
# set up release you want
asetup 21.0.108,Athena,here
# fetch run script
cp ${script_dir}/39_5050_sim.sh run.sh
export DATAPATH=$WORK/private/workingDM/simReco/data:$DATAPATH
chmod +x run.sh
perl -e "s/REPNSKIP/$nskip/g;" -pi run.sh

cp ${script_dir}/39_5050_reco.sh runReco.sh
chmod +x runReco.sh

# fetch input EVNT file
#xrdcp root://eosuser/${evnt_dir}/EVNT.01320034._000146.pool.root.1 EVNT.pool.root
cp $evnt_dir/EVNT.pool.root .


./run.sh

rm -f EVNT.pool.root
./runReco.sh

# copy your output to eg eos
mkdir -p $file_dir
cp *.pool.root $file_dir
cp log.* $file_dir
