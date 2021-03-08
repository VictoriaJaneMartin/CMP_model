from MadGraphControl.MadGraphUtils import *

######
## number of events to generate + safety margin
nevents=1.1*runArgs.maxEvents
runName='run_01'
gridpack_dir='madevent/'
gridpack_mode=False
mode=2 #mode=0 for single-core run, mode=1 if access to acluster, mode=2 for multicore production
njobs=132
cluster_type='lsf'
cluster_queue='8nh'

######

## map DSID to process settings
# select diagram removal scheme: DR1 or DR2?
DM = [ 999999 ]

if runArgs.runNumber in DM:
    print('LM Hello')
else:
    raise RuntimeError("runNumber %i not recognised in these jobOptions."%runArgs.runNumber)

######
#Chi Only Decay
#mgproc="generate p p > ~chi+ ~chi-"

# Two Body Decay
#mgproc="generate p p > ~chi+ ~chi-, (~chi+ > phi1+ ~Psi), (~chi- > phi1- ~Psi~) "#

# Three Body Decay (Muon only)
mgproc="generate p p > ~chi+ ~chi-, (~chi+ > phi1+ ~Psi , phi1+ > mu+ nn2 , phi1+ > e+ nn1 , phi1+ > ta+ nn3 ), (~chi- > phi1- ~Psi~, phi1- > mu- nn2~ , phi1- > e- nn1~ , phi1- > ta- nn3~ ) "



name='DM'
process="pp>DM"

fcard = open('proc_card_mg5.dat','w')
fcard.write("""
import model sm
# Define multiparticle labels
define p = g u c d s u~ c~ d~ s~
define j = g u c d s u~ c~ d~ s~
define l+ = e+ mu+
define l- = e- mu-
define vl = ve vm vt
define vl~ = ve~ vm~ vt~
import model ./DM
define nn = nn1 nn2 nn3
define nn~ nn1~ nn2~ nn3~
"""+mgproc+"""
output -f
""")
fcard.close()

extras = {'pdlabel'        : "'lhapdf'",
          'lhaid'          : 260000,
#          'parton_shower'  :'PYTHIA8',
          'reweight_scale' : 'True',
          'reweight_PDF'   : 'True',
          'PDF_set_min'    : 260001,
          'PDF_set_max'    : 260100,
          'bwcutoff'       : 50.,
          'fixed_ren_scale' : "False",
	  'fixed_fac_scale' : "False",
          'dynamical_scale_choice' : 3 }

runName = 'madgraph.'+str(runArgs.runNumber)+'.MadGraph_'+str(name)

beamEnergy=-999
if hasattr(runArgs,'ecmEnergy'):
    beamEnergy = runArgs.ecmEnergy / 2.
else:
    raise RuntimeError("No center of mass energy found.")

process_dir = new_process(grid_pack=gridpack_dir)

# param card
build_param_card(param_card_old=process_dir+'/Cards/param_card.dat',param_card_new='param_card_new.dat')

generate(run_card_loc='Cards/run_card_Lorenzo.dat',param_card_loc='param_card_new.dat',mode=mode,njobs=njobs,proc_dir=process_dir,run_name=runName,madspin_card_loc=None,nevents=nevents,random_seed=runArgs.randomSeed,required_accuracy=0.001)

outputDS=arrange_output(run_name=runName,proc_dir=process_dir,lhe_version=3,saveProcDir=True)


evgenConfig.description = 'DM'
runArgs.inputGeneratorFile=outputDS


# hacking LHE file

oldlhe = open(process_dir+'/Events/'+runName+'/unweighted_events.lhe','r')
newlhe = open(process_dir+'/Events/'+runName+'/unweighted_events2.lhe','w')


init = True
lhacodes = ['200001','5000001','200000','200002','200003','200004',       '-200001','-5000001','-200000','-200002','-200003','-200004']
MC_codes = ['  1000024','  1000037','  1000022','  1000012','  1000014',' 1000016',  ' -1000024',' -1000037','  1000022',' -1000012',' -1000014',' -1000016']

for line in oldlhe:
    if init==True:
        for x in range(len(lhacodes)):
            if lhacodes[x] in line:
                line = line.replace(lhacodes[x],MC_codes[x])
        newlhe.write(line)
        if '</init>' in line:
            init = False
    else:
        newline=line.rstrip('\n')
        columns=newline.split()
        pdgid=columns[0]
        no_change=True
        for old_particle, new_particle in zip(lhacodes,MC_codes):
            if(pdgid==old_particle):
                part1=new_particle
                part2=line[10:]
                newlhe.write(part1+part2)
                no_change=False
        if no_change:
            newlhe.write(line)


oldlhe.close()
newlhe.close()

zip1 = subprocess.Popen(['gzip',process_dir+'/Events/'+runName+'/unweighted_events2.lhe'])
zip1.wait()

shutil.move(process_dir+'/Events/'+runName+'/unweighted_events2.lhe.gz',process_dir+'/Events/'+runName+'/unweighted_events.lhe.gz')
os.remove(process_dir+'/Events/'+runName+'/unweighted_events.lhe')

arrange_output(run_name=runName,proc_dir=process_dir,outputDS=runName+'._00001.events.tar.gz')

import os
if 'ATHENA_PROC_NUMBER' in os.environ:
    opts.nprocs = 0
runArgs.inputGeneratorFile=runName+'._00001.events.tar.gz'

######
## shower settings: if you change these to another shower eg Hw++,
## make sure you update subtraction term ('parton_shower'  :'PYTHIA8')
include("MC15JobOptions/Pythia8_A14_NNPDF23LO_EvtGen_Common.py")
#include("MC15JobOptions/Pythia8_aMcAtNlo.py")
include("MC15JobOptions/Pythia8_SMHiggs125_inc.py")
## don't include shower weights, see ATLMCPROD-6135
#include("MC15JobOptions/Pythia8_ShowerWeights.py")
include("MC15JobOptions/Pythia8_MadGraph.py")


# Chinew is non-interacting
bonus_file = open('pdg_extras.dat','w')
bonus_file.write('200001 ~Chi+ 700.0 (GeV/c) fermion ~Chi+ 0\n')
bonus_file.write('-200001 ~Chi- 700.0 (GeV/c) fermion ~Chi- 0\n')

bonus_file.write('5000001 phi+ 250.0 (GeV/c) scalar phi+ 0\n')
bonus_file.write('-5000001 phi- 250.0 (GeV/c) scalar phi- 0\n')

bonus_file.write('200000 ~Psi 500.0 (GeV/c) fermion ~Psi 0\n')
bonus_file.write('-200000 ~Psi~ 500.0 (GeV/c) fermion ~Psi~ 0\n')



bonus_file.close()
testSeq.TestHepMC.G4ExtraWhiteFile='pdg_extras.dat'

# added from yanyan's jobOptions
genSeq.Pythia8.Commands += ["Main:timesAllowErrors = 60000"]

#relax the cuts on displaced vertices and non G4 particles
testSeq.TestHepMC.MaxTransVtxDisp = 100000000 #in mm
testSeq.TestHepMC.MaxVtxDisp = 100000000 #in mm
testSeq.TestHepMC.MaxNonG4Energy = 100000000 #in MeV
