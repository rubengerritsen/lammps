# QMMM Calculations
# 0. Set the VOTCA environment variables
```bash
source VOTCARC.bash
```
# 1. Convert CHELPG to MPS (multipole) files

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
xtp_parallel -e qmmm -o OPTIONS/qmmm.xml -f state.hdf5 -j "run"
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