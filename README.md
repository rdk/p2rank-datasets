
# Datasets for P2RANK project

These are datasets used by P2RANK ligand binding site prediction tool for training and evaluation.

Each `*.ds` file contains list of items that form a dataset with actual data being stored in subdirectories.

## Dataset types

* "standard" ... 1 column of liganated proteins
* whith predictions ... 2 columns. Includes predictions by other ligand binding site prediction methods. They are used by older PRANK algorithm for rescoring and by P2RANK for training. ("-fpocket.ds", "-sitehound.ds" suffixes) 
* with explicily specified relevant ligands ("mlig-*" prefix) based on MOAD database

## Datasets

Main sets of proteins:

* CHEN11: a dataset of 251 proteins harboring 476 ligands introduced in LBS prediction benchmarking study
* ASTEX: Astex Diverse set
* metapocket2 datasets
    - U/B48: Datasets that contain a set of 48 proteins in a bound and unbound state
    - DT198: a dataset of 198 drug-target complexes
    - B210: a benchmarking dataset of 210 proteins in bound state
* FPTRAIN: dataset used by Fpocket for training its pocket scoring function
* HOLO4K: large dataset of protein-ligand complexes. Contains larger multi chain structures downloaded directly from PDB. Disjunct with CHEN11 and JOINED. 

Variations:
* `*(mlig)*` datasets: datasets that contain explicitely specified relevant ligands. Valid ligand codes come from MOAD 2013 database. Proteins unknown to MOAD and proteins with conflicting ligand codes (valid&invalid) were removed.
* `*-shsubset` datasets: contain subset of original dataset for which SiteHound finished successfully.


# Predictions
This repository also contains binding site predictions prodused by some other methods.

* Fpocket 
    - used version: v1.0 with default parameters
* SiteHound
    - used version: version labeled as  
    - command used to generate predictions: `ls *.pdb | xargs -i python ../auto.py -i {} -p CMET -k` (executed in directory with pdb files)
    - default probe and parameters were used
* MetaPocket 2.0 
    - obtained from MetaPocket 2.0 web server by a python script in Fall 2017 using default parameters
* DeepSite
    - obtained from DeepSite web server by a python script in Fall 2017 using default parameters


# modifications

* 1xgf.pdb removed from holo4k datasets (all UNK groups, no ligands)