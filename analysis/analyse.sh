#!/bin/bash
acmSetup
cp ../CMP_Files/AnalysisAlgJobOptions.py ../source/Analysis/share/AnalysisAlgJobOptions.py
cp ../CMP_Files/MyPackageAlg.cxx ../source/Analysis/src/AnalysisAlg.cxx
cp ../CMP_Files/MyPackageAlg.h ../source/Analysis/src/AnalysisAlg.h
cp ../CMP_Files/CMakeLists.txt ../source/Analysis/CMakeLists.txt
acm compile
cd ../run
athena ../source/Analysis/share/AnalysisAlgJobOptions.py


