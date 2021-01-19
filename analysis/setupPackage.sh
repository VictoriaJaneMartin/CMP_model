#!/bin/bash
mkdir -p  build run source
cd build
acmSetup --sourcearea=../source AthAnalysis,21.2.35
acm new_skeleton Analysis

