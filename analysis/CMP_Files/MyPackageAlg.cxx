// Analysis includes
#include "AnalysisAlg.h"

//#include "xAODEventInfo/EventInfo.h"

AnalysisAlg::AnalysisAlg(const std::string &name, ISvcLocator *pSvcLocator) : AthAnalysisAlgorithm(name, pSvcLocator)
{

  //declareProperty( "Property", m_nProperty = 0, "My Example Integer Property" ); //example property declaration
}

AnalysisAlg::~AnalysisAlg() {}

StatusCode AnalysisAlg::initialize()
{
  ATH_MSG_DEBUG("Initializing " << name() << "...");
  //
  //This is called once, before the start of the event loop
  //Retrieves of tools you have configured in the joboptions go here
  //

  pt_Chis = new std::vector<float>();
  eta_Chis = new std::vector<float>();
  phi_Chis = new std::vector<float>();
  status_Chis = new std::vector<int>();
  DecVtx_x_Chi = new std::vector<float>();
  DecVtx_x_Chi = new std::vector<float>();

  pt_S = new std::vector<float>();
  eta_S = new std::vector<float>();
  phi_S = new std::vector<float>();

  pt_Psi = new std::vector<float>();
  eta_Psi = new std::vector<float>();
  phi_Psi = new std::vector<float>();

  pt_NN1 = new std::vector<float>();
  eta_NN1 = new std::vector<float>();
  phi_NN1 = new std::vector<float>();

  pt_NN2 = new std::vector<float>();
  eta_NN2 = new std::vector<float>();
  phi_NN2 = new std::vector<float>();

  pt_NN3 = new std::vector<float>();
  eta_NN3 = new std::vector<float>();
  phi_NN3 = new std::vector<float>();

  pt_muons = new std::vector<float>();
  eta_muons = new std::vector<float>();
  phi_muons = new std::vector<float>();

  pt_electrons = new std::vector<float>();
  eta_electrons = new std::vector<float>();
  phi_electrons = new std::vector<float>();

  pt_jet= new std::vector<float>();
  eta_jet = new std::vector<float>();
  phi_jet = new std::vector<float>();

  mpx = new std::vector<float>();
  mpy = new std::vector<float>();

  CHECK(book(TTree("analysisTree", "analysis ntuple")));
  TTree *ttree = tree("analysisTree");

  ttree->Branch("RunNumber", &m_runNumber);
  ttree->Branch("EventNumber", &m_eventNumber);
  ttree->Branch("pt_Chis", &pt_Chis);
  ttree->Branch("eta_Chis", &eta_Chis);
  ttree->Branch("phi_Chis", &phi_Chis);
  ttree->Branch("status_Chis", &status_Chis);
  ttree->Branch("DecVtx_x_Chi", &DecVtx_x_Chi);
  ttree->Branch("DecVtx_y_Chi", &DecVtx_y_Chi);

  ttree->Branch("pt_S", &pt_S);
  ttree->Branch("eta_S", &eta_S);
  ttree->Branch("phi_S", &phi_S);

  ttree->Branch("pt_Psi", &pt_Psi);
  ttree->Branch("eta_Psi", &eta_Psi);
  ttree->Branch("phi_Psi", &phi_Psi);

  ttree->Branch("pt_NN1", &pt_NN1);
  ttree->Branch("eta_NN1", &eta_NN1);
  ttree->Branch("phi_NN1", &phi_NN1);

  ttree->Branch("pt_NN2", &pt_NN2);
  ttree->Branch("eta_NN2", &eta_NN2);
  ttree->Branch("phi_NN2", &phi_NN2);

  ttree->Branch("pt_NN3", &pt_NN3);
  ttree->Branch("eta_NN3", &eta_NN3);
  ttree->Branch("phi_NN3", &phi_NN3);

  ttree->Branch("pt_muons", &pt_muons);
  ttree->Branch("eta_muons", &eta_muons);
  ttree->Branch("phi_muons", &phi_muons);

  ttree->Branch("pt_electrons", &pt_electrons);
  ttree->Branch("eta_electrons", &eta_electrons);
  ttree->Branch("phi_electrons", &phi_electrons);

  ttree->Branch("pt_jet", &pt_jet);
  ttree->Branch("eta_jet", &eta_jet);
  ttree->Branch("phi_jet", &phi_jet);

  ttree->Branch("mpx", &mpx);
  ttree->Branch("mpy", &mpy);

  return StatusCode::SUCCESS;
}

StatusCode AnalysisAlg::finalize()
{
  ATH_MSG_INFO("Finalizing " << name() << "...");
  //
  //Things that happen once at the end of the event loop go here
  //
  delete pt_Chis;
  delete eta_Chis;
  delete phi_Chis;
  delete status_Chis;
  delete DecVtx_x_Chi;
  delete DecVtx_y_Chi;

  delete pt_S;
  delete eta_S;
  delete phi_S;

  delete pt_Psi;
  delete eta_Psi;
  delete phi_Psi;

  delete pt_NN1;
  delete eta_NN1;
  delete phi_NN1;

  delete pt_NN2;
  delete eta_NN2;
  delete phi_NN2;

  delete pt_NN3;
  delete eta_NN3;
  delete phi_NN3;

  delete pt_muons;
  delete eta_muons;
  delete phi_muons;

  delete pt_electrons;
  delete eta_electrons;
  delete phi_electrons;

  delete pt_jet;
  delete eta_jet;
  delete phi_jet;

  delete mpx;
  delete mpy;

  return StatusCode::SUCCESS;
}

StatusCode AnalysisAlg::execute()
{
  ATH_MSG_INFO("Executing " << name() << "...");
  setFilterPassed(false); //optional: start with algorithm not passed

  pt_Chis->clear();
  eta_Chis->clear();
  phi_Chis->clear();
  status_Chis->clear();
  DecVtx_x_Chi->clear();
  DecVtx_y_Chi->clear();

  pt_S->clear();
  eta_S->clear();
  phi_S->clear();

  pt_Psi->clear();
  eta_Psi->clear();
  phi_Psi->clear();

  pt_NN1->clear();
  eta_NN1->clear();
  phi_NN1->clear();

  pt_NN2->clear();
  eta_NN2->clear();
  phi_NN2->clear();

  pt_NN1->clear();
  eta_NN1->clear();
  phi_NN1->clear();

  pt_muons->clear();
  eta_muons->clear();
  phi_muons->clear();

  pt_electrons->clear();
  eta_electrons->clear();
  phi_electrons->clear();

  pt_jet->clear();
  eta_jet->clear();
  phi_jet->clear();

  mpx->clear();
  mpy->clear();

  chis.clear();
  Scalar.clear();
  Psi.clear();
  NN1.clear();
  NN2.clear();
  NN3.clear();



  const xAOD::EventInfo *eventInfo = nullptr;
  CHECK(evtStore()->retrieve(eventInfo, "EventInfo"));
  m_runNumber = eventInfo->runNumber();
  m_eventNumber = eventInfo->eventNumber();

  // ATH_MSG_INFO("Run number: " << m_runNumber << "; Event number: " << m_eventNumber);

  const xAOD::TruthParticleContainer *parts = nullptr;
  CHECK(evtStore()->retrieve(parts, "TruthParticles"));

  for (auto p : *parts)
  {
    if (1000024 == abs(p->pdgId()))
    {
      status_Chis->push_back(p->status());
      if (p->status() == 22)
      {
        pt_Chis->push_back(p->pt());
        eta_Chis->push_back(p->eta());
        phi_Chis->push_back(p->phi());
        chis.push_back(p->p4());
      if (p->hasDecayVtx() ==1){
        DecVtx_x_Chi->push_back(p->decayVtx()->x());
        DecVtx_y_Chi->push_back(p->decayVtx()->y());
      }
      }

    }
    if (1000037 == abs(p->pdgId()))
    {
      if (p->status() == 1)
      {
        pt_S->push_back(p->pt());
        eta_S->push_back(p->eta());
        phi_S->push_back(p->phi());
        Scalar.push_back(p->p4());
      }

    }
    if (1000022 == abs(p->pdgId()))
    {
      if (p->status() == 1)
      {
        pt_Psi->push_back(p->pt());
        eta_Psi->push_back(p->eta());
        phi_Psi->push_back(p->phi());
        Psi.push_back(p->p4());
      }

    }

    if (1000012 == abs(p->pdgId()))
    {
      if (p->status() == 1)
      {
        pt_NN1->push_back(p->pt());
        eta_NN1->push_back(p->eta());
        phi_NN1->push_back(p->phi());
        NN1.push_back(p->p4());
      }

    }
    if (1000014 == abs(p->pdgId()))
    {
      if (p->status() == 1)
      {
        pt_NN2->push_back(p->pt());
        eta_NN2->push_back(p->eta());
        phi_NN2->push_back(p->phi());
        NN2.push_back(p->p4());
      }

    }
    if (1000016 == abs(p->pdgId()))
    {
      if (p->status() == 1)
      {
        pt_NN3->push_back(p->pt());
        eta_NN3->push_back(p->eta());
        phi_NN3->push_back(p->phi());
        NN3.push_back(p->p4());
      }

    }
  }

  const xAOD::MuonContainer *muon_parts = nullptr;
  CHECK(evtStore()->retrieve(muon_parts, "Muons"));

  for (auto p : *muon_parts)
  {

    pt_muons->push_back(p->pt());
    eta_muons->push_back(p->eta());
    phi_muons->push_back(p->phi());


  const xAOD::ElectronContainer *electron_parts = nullptr;
  CHECK(evtStore()->retrieve(electron_parts, "Electrons"));

  for (auto p : *electron_parts)
  {
    pt_electrons->push_back(p->pt());
    eta_electrons->push_back(p->eta());
    phi_electrons->push_back(p->phi());


  const xAOD::JetContainer *partsJet = nullptr;
  CHECK(evtStore()->retrieve(partsJet, "AntiKt4EMPFlowJets"));

  for (auto p : *partsJet)
  {
    pt_jet->push_back(p->pt());
    eta_jet->push_back(p->eta());
    phi_jet->push_back(p->phi());
  }

  const xAOD::MissingETContainer *partsET = nullptr;
  CHECK(evtStore()->retrieve(partsET, "MET_Core_AntiKt4EMPFlow"));

  for (auto p : *partsET)
  {
    mpx->push_back(p->mpx());
    mpy->push_back(p->mpy());
  }

  tree("analysisTree")->Fill();

  setFilterPassed(true); //if got here, assume that means algorithm passed
  return StatusCode::SUCCESS;
}

StatusCode AnalysisAlg::beginInputFile()
{
  //
  //This method is called at the start of each input file, even if
  //the input file contains no events. Accumulate metadata information here
  //

  //example of retrieval of CutBookkeepers: (remember you will need to include the necessary header files and use statements in requirements file)
  // const xAOD::CutBookkeeperContainer* bks = 0;
  // CHECK( inputMetaStore()->retrieve(bks, "CutBookkeepers") );

  //example of IOVMetaData retrieval (see https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/AthAnalysisBase#How_to_access_file_metadata_in_C)
  //float beamEnergy(0); CHECK( retrieveMetadata("/TagInfo","beam_energy",beamEnergy) );
  //std::vector<float> bunchPattern; CHECK( retrieveMetadata("/Digitiation/Parameters","BeamIntensityPattern",bunchPattern) );

  return StatusCode::SUCCESS;
}
