# Run arguments file auto-generated on Sun Oct  4 10:13:52 2020 by:
# JobTransform: generate
# Version: $Id: trfExe.py 814151 2018-05-15 16:57:00Z mavogel $
# Import runArgs class
from PyJobTransforms.trfJobOptions import RunArguments
runArgs = RunArguments()
runArgs.trfSubstepName = 'generate' 

runArgs.randomSeed = 123456
runArgs.generatorJobNumber = 0
runArgs.printEvts = 5
runArgs.runNumber = 999999
runArgs.skipEvents = 0
runArgs.maxEvents = 10
runArgs.jobConfig = ['MC15.999999.MadGraphPythia8EvtGen_NNPDF23LO_DM.py']
runArgs.generatorRunMode = 'run'
runArgs.firstEvent = 1
runArgs.ecmEnergy = 13000.0

# Input data

# Output data
runArgs.outputEVNTFile = 'EVNT.pool.root'
runArgs.outputEVNTFileType = 'EVNT'

# Extra runargs

# Extra runtime runargs

# Literal runargs snippets
