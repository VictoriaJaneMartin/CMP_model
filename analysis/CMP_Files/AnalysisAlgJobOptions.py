#Skeleton joboption for a simple analysis job

#---- Minimal job options -----

jps.AthenaCommonFlags.AccessMode = "ClassAccess"              #Choose from TreeAccess,BranchAccess,ClassAccess,AthenaAccess,POOLAccess
#jps.AthenaCommonFlags.TreeName = "MyTree"                    #when using TreeAccess, must specify the input tree name

jps.AthenaCommonFlags.HistOutputs = ["ANALYSIS:ntuple.root"]  #register output files like this. MYSTREAM is used in the code

athAlgSeq += CfgMgr.AnalysisAlg()                               #adds an instance of your alg to the main alg sequence


#---- Options you could specify on command line -----
#jps.AthenaCommonFlags.EvtMax=-1                          #set on command-line with: --evtMax=-1
#jps.AthenaCommonFlags.SkipEvents=0                       #set on command-line with: --skipEvents=0
jps.AthenaCommonFlags.FilesInput = ["/afs/cern.ch/user/j/jdykstra/public/CMP_model/analysis/source/DAOD_PASSTHR.DAOD.root"]        #set on command-line with: --filesInput=...
#jps.AthenaCommonFlags.FilesInput = ["/afs/cern.ch/work/l/lprincip/private/workingDM/oldAnalysis/inputFile/DAOD_PASSTHR.20200312_1000evts.rightNum.pool.root"]

#include("AthAnalysisBaseComps/SuppressLogging.py")              #Optional include to suppress as much athena output as possible. Keep at bottom of joboptions so that it doesn't suppress the logging of the things you have configured above
