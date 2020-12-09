# Defining shortcut functions
# Used aliases
alias asetup_gen="asetup 19.2.5.33.4,MCProd,64,here --cmtconfig=x86_64-slc6-gcc47-opt"
alias asetup_sim="asetup 21.0.108,Athena,here"
alias asetup_reco=$asetup_sim

export workingDir="/afs/cern.ch/user/j/jdykstra/public/CMP_model"


# Shortcut functions
# for generation
alias generate="source $workingDir/gen/generate.sh $*"

# for simulation
alias simulate="source $workingDir/simReco/simulate.sh $*"

# for reconstruction
alias reco="source $workingDir/simReco/reco.sh $*"

# for analysis
alias analysis="athena Analysis/share/AnalysisAlgJobOptions.py $*"
alias buildAnalysis="acm compile && analysis $*"
