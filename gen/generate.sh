#/bin/bash

# Determine run parameters
jo=MC15.999999.MadGraphPythia8EvtGen_NNPDF23LO_DM.py
ecmEnergy=13000. 
maxEvents=10000
skipEvents=0
randomSeed=123456 
outputEVNTFile=EVNT.pool.root


workingDir=`pwd`
baseDir=Base
dirName="here"

if [ $dirName = "here" ]
then
	echo "Running process in default directory genProcess"
	dirName=genProcess
	mkdir $dirName
elif [ ! -d $dirName ]
then
	echo "Making directory $dirName"
	mkdir $dirName
fi

cp -r $baseDir/* $workingDir/$dirName

cd $dirName

echo "Parameters for $dirName run

ecmEnergy = $ecmEnergy
jo=$jo
maxEvents=$maxEvents
randomSeed=$randomSeed
outputEVNTFile=$outputEVNTFile" >>README.md

Generate_tf.py \
	--ecmEnergy=$ecmEnergy\
	--runNumber=$(echo $jo |cut -d. -f2) \
	--maxEvents=$maxEvents \
	--randomSeed=$randomSeed \
	--outputEVNTFile=$outputEVNTFile \
	--skipEvents=$skipEvents \
	--jobConfig $jo



echo "Generation ended in directory $dirName"
