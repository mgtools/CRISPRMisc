A repository containing the data and programs for studying CRISPR-Cas and AMR genes in healthcare-related pathogens

To download/visualize identified CRISPR-Cas systems, please go to <a href="https://omics.informatics.indiana.edu/CRISPRone/pathogen/">CRISPRone</a> website.

What's included in this repository:

* Data
  * tables/*: tables showing the presence of CRISPR-Cas systems and the number of predicted AMR genes in the different isolates of each species
  * data/amrplus_eskape.csv.gz: predicted AMR genes in all pathogen isolates

* Programs
  * CRISPR-AMR-test.ipynb: a python notebook for statistical testing if CRISPR-Cas containing isolates tend to have fewer AMR genes
  * lib/build_spacer2mge_network.py: script that takes spacer blast outputs and spacer cdhit outputs and constructs a MGE:spacer network

* Example: build MGE:spacer network

  > python lib/build_spacer2mge_network.py <br>
  >      --phage blast_output/example_phages.filtered.derep.m8 <br>
  >      --plasmid build_network_example/blast_output/example_plasmids.filtered.derep.m8 <br>
  >      -c build_network_example/cdhit_out/example_cdhit0.85.clstr <br>
  >      -o build_network_example/example.gml


Reference: Comparison of CRISPR–Cas immune systems in healthcare-related pathogens" by Kate Mortensen, Tony Lam and Yuzhen Ye (submitted)
