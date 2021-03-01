#!/bin/bash
root EVNT.pool.root <<EOF 
new TH1F("myhist", "myhist",21,1000020,1000040);
CollectionTree->Draw("McEventCollection_p5_GEN_EVENT.m_genParticles.m_pdgId>>myhist");

myhist->SaveAs(“hist1.pdf”,“pdf”);
gSystem->Sleep(111000);
EOF

