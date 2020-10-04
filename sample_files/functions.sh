# Defining shortcut functions
alias asetup_gen="asetup 19.2.5.33.4,MCProd,64,here --cmtconfig=x86_64-slc6-gcc47-opt"
alias generate="source /afs/cern.ch/user/l/lprincip/public/workingDM/gen/generate.sh $*"
alias asetup_sim="asetup 21.0.108,Athena,here"
alias simulate="source /afs/cern.ch/user/l/lprincip/public/workingDM/simReco/simulate.sh $*"
alias asetup_reco=$asetup_sim
alias reco="source /afs/cern.ch/user/l/lprincip/public/workingDM/simReco/reco.sh $*"
alias analysis="athena Analysis/AnalysisAlgJobOptions.py $*"

toCernbox(){
    if [[ $# -lt 1 ]]; then
        echo "Usage: ${FUNCNAME[0]} <file to copy> [<other files to copy>]"
        return 1
    fi

    for item in $*; do
        cp -r $item $CERNBOX/autoCp/

        if [[ $? -eq 0 ]]; then
            echo "Copied $item to $CERNBOX/autoCP"
        fi
    done
}

buildAnalysis(){
  acm compile && analysis $*
        
}
