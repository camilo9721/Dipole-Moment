# Dipole-Moment

Bash and Python scripts needed to handle information for the dipole moment project.

  change.sh: change the basis set used in the computations for the augmented versions of the Pople-style basis sets (6-31G*,     6-31+G, etc.). This is is needed because they cannot be created with the Snakemake flow file.
  
  outputs.sh: extracts all output files from their respective folders and place them into a new folder named as /Results.
  
  proc.py: extracts relevant information from the output files and storage it into a new file names as results.txt
  
  runall.sh: runs the proc.py file for all output fules within the /Results folder.
