# QMMM Calculations with VOTCA and LAMMPS
The basic input files for this tutorial where calculated with the ORCA dft package. In the `DFT_ORCA` folder are the results and the input files that generated them, a short description of the process can be found in `AUXILIARY/ORCA_dft_calculations.md`.

The MD trajectory was generated with LAMMPS, the relevant data can be found in the `LAMMPS` directory.
# 0. Set the VOTCA environment variables
```bash
source VOTCARC.bash
```
# 1. Convert CHELPG to MPS (multipole) files
The MPS files are stored in the `MP_FILES` directory.
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

# 2. Mapping and State Creation

### Create the state file from the LAMMPS topology
```bash
xtp_map -t LAMMPS/system.data -c LAMMPS/traj1.dump -s OPTIONS/mapping.xml -f state.hdf5
```

### Run Map Checker
```bash
xtp_run -e mapchecker -o OPTIONS/mapchecker.xml -f state.hdf5
```

# 3. Create the QM/MM calculation
### Create QMMM jobs
```bash
xtp_parallel -e qmmm -o OPTIONS/qmmm.xml -f state.hdf5 -j "write"
```
### Perform the QMMM jobs
```bash
xtp_parallel -e qmmm -o OPTIONS/qmmm.xml -f state.hdf5 -j "run" -t <nrOfProcesses> -x <threadsPerProcess>
xtp_parallel -e qmmm -o OPTIONS/qmmm.xml -f state.hdf5 -j "run" -x 6
```

### Load the results in the state file
```bash
xtp_parallel -e qmmm -o OPTIONS/qmmm.xml -f state.hdf5 -j "read"
```

# 4. Results

Check the contents of `qmmm_jobs.xml`

# 5. Appendix: Useful commands
Check the description of a tool

```bash
xtp_tools -d <tool_name>
```

Print (`-p`) **all** options to an example option file (`-o`).

```bash
xtp_tools -p <tool_name> -o <option_file_name>.xml
```