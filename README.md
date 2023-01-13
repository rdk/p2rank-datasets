
# Datasets for P2Rank project

These are datasets used by P2Rank ligand binding site prediction tool for training and evaluation.

Each `*.ds` file contains list of items that form a dataset with actual data being stored in subdirectories.

## ! Important note !

Please note that `*.ds` files that define the datasets from our papers may contain only subsets of PDB files in individual directories. For example holo4k/ directory contains 4543 pdb files but `holo4k.ds` contains 4009 lines. For reproducibility, 4009 is the correct number of proteins in the HOLO4K dataset from the papers. 


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

### Variations 
* "standard" ... 1 column of liganated proteins 
* `*(mlig)*` datasets: datasets that contain explicitly specified relevant ligands. Valid ligand codes come from MOAD 2013 database. Proteins unknown to MOAD and proteins with conflicting ligand codes (valid&invalid) were removed. 
* datasets with predictions: include predictions by other ligand binding site prediction methods
(`-fpocket.ds`, `-sitehound.ds`, etc. suffixes)  
* `*-XXsubset-*` datasets: contain subset of original dataset for which given method finished successfully and produced predictions (`mp`:
MetaPocket2, `sh`: SiteHound, `ds`: DeepSite)


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
* P2Rank
    - correspond to P2Rank 2.0 with default parameters

# modifications

* 1xgf.pdb removed from holo4k datasets (all UNK groups, no ligands)
