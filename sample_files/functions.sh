# Defining shortcut functions
# Used aliases
alias asetup_gen="asetup 19.2.5.33.4,MCProd,64,here --cmtconfig=x86_64-slc6-gcc47-opt"
alias asetup_sim="asetup 21.0.108,Athena,here"
alias asetup_reco=$asetup_sim

# Shortcut functions
export workingDir="/afs/cern.ch/user/l/lprincip/public/workingDM"
alias generate="source $workingDir/gen/generate.sh $*"
alias simulate="source $workingDir/simReco/simulate.sh $*"
alias reco="source $workingDir/simReco/reco.sh $*"
alias analysis="athena Analysis/AnalysisAlgJobOptions.py $*"

alias buildAnalysis="acm compile && analysis $*"