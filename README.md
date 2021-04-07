# Implementation of an efficient SARS-CoV-2 pooled testing strategy for high throughput diagnostic testing: pooling scripts

## Overview

This repository is a set of scripts for Opentrons OT-2 pipetting robot.

1. files pooling27_50pip.py & pooling27_300pip.py contain scripts for the hypercube of the size 27 for a 50 microliter and 300 microliters, respectively.

2. files pooling81_50pip.py & pooling81_300pip.py contain scripts for the hypercube of the size 81 for a 50 microliter and 300 microliters, respectively.

The scripts are designed for custom Lab Plate (8x12). One can use the standard Opentron plates of the same size.

3. files positive_results_v1.py and positive_results_v2.py contain scripts to infer positive results. V1 does not take into account degenerates but can still infer more than one positive per pool at low prevalence while V2 considers degenerates. 

## System / OS requirements

The scripts are developed using the Python programming language that is platform independent. They will therefore run normally on any system with Python 3 interpreter.

## How to execute 

To the run the scripts;

The pooling27 and pooling81 scripts should be [deployed](https://docs.opentrons.com/v2/writing.html) on the instrument i.e. according to the standard opentrons [guidelines](https://docs.opentrons.com/v2/writing.html). Once deployed, the protocol can then be calibrated and used to perform pooling experiments.

To run the scripts to infer positives (test data available in the data folder);

```
python 	positive_results_v1.py
```

The program will then request for user input to be entered interactively via the command prompt. Once all the user input has been provided, it will infer and printout the positive result to stdout.

## License

This project is covered under the MIT License

## Citation

TBD