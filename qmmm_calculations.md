# QMMM Calculations
Source votca
```bash
setupVotcaSoft
```

## Create Input Files with ORCA
We determine the groundstate geometry with orca

```text 
!PBE0 def2-TZVP OPT

*xyz 0 1
O  0.006  -0.848   0.086
C -0.873  -1.710  -0.085  
C -1.406  -2.648   0.972 
C -1.572  -1.974  -1.412 
H -1.093  -2.515   1.991  
H -2.463  -2.735   1.032 
H -1.069  -3.613   0.608 
H -0.905  -1.801  -2.305 
H -2.474  -1.426  -1.590 
H -1.800  -3.000  -1.522 
*

%pal
 nprocs 26
end
```

### Next use CHELPG to do a charge fit 
```text
!PBE0 def2-TZVP CHELPG

*xyzfile 0 1 acetoneOpt.xyz

%pal
 nprocs 26
end

%elprop
Polar 1
end
```

### Do the same for water

## Convert CHELPG to MPS (multipole) files

```bash
cd MP_FILES
xtp_tools -e log2mps -o OPTIONS/log2mps_acetone.xml
xtp_tools -e log2mps -o OPTIONS/log2mps_water.xml
```

### Scale the polarizability

```bash
xtp_tools -e molpol -o OPTIONS/molpol_acetone.xml
xtp_tools -e molpol -o OPTIONS/molpol_water.xml
```

# Setup and Start the QMMM calc

### Create the state file from the LAMMPS topology
```bash
xtp_map -v -t system.data -c traj1.dump -s mapping.xml -f state.hdf5
```

### Run Map Checker
```bash
xtp_run -e mapchecker -o mapchecker.xml -f state.hdf5
```

### Create QMMM jobs


### Delete all unnecessary jobs

### Perform QMMM calc


## Make a picture

requires some python packages which can be pip installed:

* numpy
* matplotlib
* tabulate

then run

```bash
python3 spectrumPlot.py
```