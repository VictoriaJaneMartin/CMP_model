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

  m_matchedMuons = new std::vector<int>();
  m_matchedElectrons = new std::vector<int>();
  actual_muons = new std::vector<int>();
  actual_electrons = new std::vector<int>();

  pt_Chis = new std::vector<float>();
  eta_Chis = new std::vector<float>();
  phi_Chis = new std::vector<float>();

  pt_S = new std::vector<float>();
  eta_S = new std::vector<float>();
  phi_S = new std::vector<float>();

  pt_Psi = new std::vector<float>();
  eta_Psi = new std::vector<float>();
  phi_Psi = new std::vector<float>();

  pt_muons = new std::vector<float>();
  eta_muons = new std::vector<float>();
  phi_muons = new std::vector<float>();
  pt_electrons = new std::vector<float>();
  eta_electrons = new std::vector<float>();
  phi_electrons = new std::vector<float>();
  mu_Eloss = new std::vector<float>();

  CHECK(book(TTree("analysisTree", "analysis ntuple")));
  TTree *ttree = tree("analysisTree");

  ttree->Branch("RunNumber", &m_runNumber);
  ttree->Branch("EventNumber", &m_eventNumber);
  ttree->Branch("pt_Chis", &pt_Chis);
  ttree->Branch("eta_Chis", &eta_Chis);
  ttree->Branch("phi_Chis", &phi_Chis);

  ttree->Branch("pt_S", &pt_S);
  ttree->Branch("eta_S", &eta_S);
  ttree->Branch("phi_S", &phi_S);

  ttree->Branch("pt_Psi", &pt_Psi);
  ttree->Branch("eta_Psi", &eta_Psi);
  ttree->Branch("phi_Psi", &phi_Psi);

  ttree->Branch("m_matchedMuons", &m_matchedMuons);
  ttree->Branch("actual_muon", &actual_muons);
  ttree->Branch("pt_muons", &pt_muons);
  ttree->Branch("eta_muons", &eta_muons);
  ttree->Branch("phi_muons", &phi_muons);
  ttree->Branch("Muons_eLoss", &mu_Eloss);
  ttree->Branch("m_matchedElectrons", &m_matchedElectrons);
  ttree->Branch("actual_electron", &actual_electrons);
  ttree->Branch("pt_electrons", &pt_electrons);
  ttree->Branch("eta_electrons", &eta_electrons);
  ttree->Branch("phi_electrons", &phi_electrons);

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
  delete pt_S;
  delete eta_S;
  delete phi_S;
  delete pt_Psi;
  delete eta_Psi;
  delete phi_Psi;
  delete m_matchedMuons;
  delete pt_muons;
  delete eta_muons;
  delete phi_muons;
  delete actual_muons;
  delete actual_electrons;
  delete m_matchedElectrons;
  delete pt_electrons;
  delete eta_electrons;
  delete phi_electrons;
  delete mu_Eloss;

  return StatusCode::SUCCESS;
}

StatusCode AnalysisAlg::execute()
{
  ATH_MSG_INFO("Executing " << name() << "...");
  setFilterPassed(false); //optional: start with algorithm not passed

  pt_Chis->clear();
  eta_Chis->clear();
  phi_Chis->clear();

  pt_S->clear();
  eta_S->clear();
  phi_S->clear();

  pt_Psi->clear();
  eta_Psi->clear();
  phi_Psi->clear();

  m_matchedMuons->clear();
  pt_muons->clear();
  eta_muons->clear();
  phi_muons->clear();
  actual_muons->clear();
  mu_Eloss->clear();

  actual_electrons->clear();
  m_matchedElectrons->clear();
  pt_electrons->clear();
  eta_electrons->clear();
  phi_electrons->clear();
  chis.clear();
  Scalar.clear();
  Psi.clear();
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
      if (p->status() == 1)
      {
        pt_Chis->push_back(p->pt());
        eta_Chis->push_back(p->eta());
        phi_Chis->push_back(p->phi());
        chis.push_back(p->p4());
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
  }

  const xAOD::MuonContainer *muon_parts = nullptr;
  CHECK(evtStore()->retrieve(muon_parts, "Muons"));

  for (auto p : *muon_parts)
  {

    pt_muons->push_back(p->pt());
    eta_muons->push_back(p->eta());
    phi_muons->push_back(p->phi());

    matchedMuon = 0;
    for (auto &i : chis)
    {
      Double_t angle = i.DeltaR(p->p4());
      if (angle <= 0.1)
      {
        matchedMuon = 1;
      }
    }

    const xAOD::TruthParticle *matched_truth_muon = nullptr;
    int actual_muon = 0;

    if (p->isAvailable<ElementLink<xAOD::TruthParticleContainer>>("truthParticleLink"))
    {
      ElementLink<xAOD::TruthParticleContainer> link = p->auxdata<ElementLink<xAOD::TruthParticleContainer>>("truthParticleLink");
      if (link.isValid())
      {
        matched_truth_muon = *link;
        if (abs(matched_truth_muon->pdgId()) == 13)
        {
          actual_muon = 1;
        }
      }
    }

    float eLoss = 0;
    if (!p->parameter(eLoss, xAOD::Muon::EnergyLoss)){
      std::cout << "Muon energy loss not available" << std::endl;
    }

    mu_Eloss->push_back(eLoss);
    actual_muons->push_back(actual_muon);
    m_matchedMuons->push_back(matchedMuon);
  }

  const xAOD::ElectronContainer *electron_parts = nullptr;
  CHECK(evtStore()->retrieve(electron_parts, "Electrons"));

  for (auto p : *electron_parts)
  {
    pt_electrons->push_back(p->pt());
    eta_electrons->push_back(p->eta());
    phi_electrons->push_back(p->phi());

    const xAOD::TruthParticle *matched_truth_electron = nullptr;
    int actual_electron = 0;

    if (p->isAvailable<ElementLink<xAOD::TruthParticleContainer>>("truthParticleLink"))
    {
      ElementLink<xAOD::TruthParticleContainer> link = p->auxdata<ElementLink<xAOD::TruthParticleContainer>>("truthParticleLink");
      if (link.isValid())
      {
        matched_truth_electron = *link;
        if (abs(matched_truth_electron->pdgId()) == 11)
        {
          actual_electron = 1;
        }
      }
    }
    actual_electrons->push_back(actual_electron);

    matchedElectron = 0;
    for (auto &i : chis)
    {
      Double_t angle = i.DeltaR(p->p4());
      if (angle <= 0.1)
      {
        matchedElectron = 1;
      }
    }

    m_matchedElectrons->push_back(matchedElectron);
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
