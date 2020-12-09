#!/bin/bash

export maxEvents=100
export skipEvents=0
export conditionsTag="default:OFLCOND-MC16-SDR-14"
export DBRelease="all:current"
export geometryVersion="default:ATLAS-R2-2016-01-00-01_VALIDATION"
export postInclude="default:RecJobTransforms/UseFrontier.py"
export preExec1="'EVNTtoHITS:simFlags.SimBarcodeOffset.set_Value_and_Lock(200000)'"
export preExec2="EVNTtoHITS:simFlags.ExtraParticlesPDGTABLE='extra.mod'"
export preExec3="EVNTtoHITS:simFlags.TRTRangeCut=30.0;simFlags.TightMuonStepping=True"
export preInclude="EVNTtoHITS:SimulationJobOptions/preInclude.BeamPipeKill.py,SimulationJobOptions/preInclude.FrozenShowersFCalOnly.py,SimulationJobOptions/preInclude.ExtraParticles.py"
export INPUT_LOCAL=""
export INPUT=user.jdykstra:genProcess.gen.dataset
export OUTPUT_LOCAL="HITS.pool.root"
export OUTPUT=user.jdykstra.20200311_1000evt_01

export DATAPATH=/afs/cern.ch/user/j/jdykstra/public/CMP_model/simReco/data:$DATAPATH



if [ "$1" == '-p' ]
then
	lsetup panda
	pathena --trf "Sim_tf.py \
    --AMITag=s3126 \
    --conditionsTag $conditionsTag\
    --DataRunNumber=284500 \
    --DBRelease $DBRelease \
    --geometryVersion=$geometryVersion \
    --physicsList=FTFP_BERT_ATL_VALIDATION \
    --postInclude $postInclude \
    --preExec $preExec1 \
              $preExec2 \
              $preExec3 \
    --preInclude $preInclude \
    --runNumber=448040 \
    --simulator=FullG4 \
    --truthStrategy=MC15aPlus \
    --inputEVNTFile %IN \
    --outputHITSFile %OUT.HITS.pool.root \
    --maxEvents $maxEvents \
    --skipEvents $skipEvents" \
    --inDS $INPUT --outDS $OUTPUT1
else


    if [[ -z $INPUT_LOCAL ]]; then
        INPUT_LOCAL="EVNT.pool.root"
        cp /afs/cern.ch/user/j/jdykstra/public/CMP_model/gen/genProcess/EVNT.pool.root ./
    fi

	Sim_tf.py \
    --AMITag=s3126 \
    --conditionsTag $conditionsTag\
    --DataRunNumber=284500 \
    --DBRelease $DBRelease \
    --geometryVersion=$geometryVersion \
    --physicsList=FTFP_BERT_ATL_VALIDATION \
    --postInclude $postInclude \
    --preExec $preExec1 \
              $preExec2 \
              $preExec3 \
    --preInclude $preInclude \
    --runNumber=448040 \
    --simulator=FullG4 \
    --truthStrategy=MC15aPlus \
    --inputEVNTFile $INPUT_LOCAL \
    --outputHITSFile $OUTPUT_LOCAL \
    --maxEvents $maxEvents \
    --skipEvents $skipEvents
fi
