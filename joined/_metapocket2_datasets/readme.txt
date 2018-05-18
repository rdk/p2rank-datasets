
Datasets from metaPocket 2.0 study *.
Downloaded from http://projects.biotec.tu-dresden.de/metapocket/benchmark.php 14 Nov 2014

    - Zengming Zhang, Yu Li, Biaoyang Lin, Michael Schroeder and Bingding Huang (2011), Identification of cavities on protein surface using multiple computational approaches for drug binding site prediction. Bioinformatics, 27 (15): 2083-2088. 

PDB files were ammended with fix-elements.groovy that adds missing element column.


====


Benchmark Data-sets used in metaPocket 2.0

1. 48 bound/unbound structures

For a realistic evaluation taking the flexibility of structures into account, we need bound and unbound structures. This dataset was derived from many previous datasets, for the detailed information of this dataset, please refer to our previous publication:

Huang, B. and M. Schroeder (2006). "LIGSITEcsc: predicting ligand binding sites using the Connolly surface and degree of conservation." BMC Struct Biol 6: 19. PubMed Link

2. 210 bound structures

This dataset was derived from the Protein Ligand Database (PLD) (PubMed Link), which was the largest hand-curated database containing all the protein-ligand complex structures available in the PDB at that time. After removing the redundant structures and selecting those having conservation scores in the ConSurf-HSSP database (PubMed Link), the result was a data-set of 210 structrures. For the detailed information of this dataset, please refer to our previous publication:

Huang, B. and M. Schroeder (2006). "LIGSITEcsc: predicting ligand binding sites using the Connolly surface and degree of conservation." BMC Struct Biol 6: 19. PubMed Link

3. 198 drug-target dataset

This dataset was derived from DrugPort, DrugBank and the PDB, and it was firstly used in metaPocket 2.0. In order to identify drug-binding sites, we built a novel dataset of drug-target complex structures available in PDB. To our knowledge, DrugPort database contains the information of protein-ligand complexes where the bound ligands are approved drugs reported in DrugBank. In the first step, we derive all drug-target pairs from DrugPort website. For each pair, we retrieve the UniProt ID for the target and link it to PDB and get the PDB file and check whether it contains both protein target and drug ligand. Only one complex structure is selected for each drug-target pair and we only keep the single chain where ligands bind. At the end of this step, we obtained 217 pairs and 96 types of drugs. In the next step, we used CD-HIT program to remove the redundancy of protein targets using 40% similarity threshold. Finally 198 drug-target complexes are obtained.