#/bin/bash

workingDir=$pwd
baseDir=$WORK/private/workingDM/gen/Base
dirName=$1

while [ -z $dirName ]
do
	echo "Which directory should the process be run in? (Type 'here' for default in current dir)"
	ls
	read dirName
done

if [ $dirName = "here" ]
	echo "Running process in default directory genProcess"
	dirName=genProcess
	mkdir $dirName
elif [ ! -d $dirName ]
then
	echo "Making directory $dirName"
	mkdir $dirName
fi

cp -r $baseDir/* $workingDir/$dirName/

cd $dirName

jo=MC15.999999.MadGraphPythia8EvtGen_NNPDF23LO_DM.py

prun --trf "Generate_tf.py \
	--ecmEnergy=13000. \
	--runNumber=$(echo $jo |cut -d. -f2) \
	--maxEvents=1 \
	--randomSeed=123456 \
	--outputEVNTFile=EVNT.pool.root \
	--jobConfig $jo



echo "Generation ended in directory $dirName"
