# Implementation of an efficient SARS-CoV-2 pooled testing strategy for high throughput diagnostic testing: pooling scripts

This repository is a set of scripts for Opentrons OT-2 pipetting robot.

1. files pooling27_50pip.py & pooling27_300pip.py contain scripts for the hypercube of the size 27 for a 50 microliter and 300 microliters, respectively.

2. files pooling81_50pip.py & pooling81_300pip.py contain scripts for the hypercube of the size 81 for a 50 microliter and 300 microliters, respectively.

The scripts are designed for custom Lab Plate (8x12). One can use the standard Opentron plates of the same size.

3. files positive_results_v1.py and positive_results_v2.py contain scripts to infer positive results. V1 does not take into account degenerates but can still infer more than one positive per pool at low prevalence while V2 considers degenerates. 



