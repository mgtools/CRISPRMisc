#!/bin/bash

python3 ../lib/build_spacer2mge_network.py --phage blast_output/example_phages.filtered.derep.m8 --plasmid blast_output/example_plasmids.filtered.derep.m8 -c cdhit_out/example_cdhit0.85.clstr -o example.gml
