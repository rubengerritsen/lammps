#!/bin/bash

module load intel
source /home/ruben/Software/votca/bin/VOTCARC.bash

for ITER in 1 2 3 .. 120
do
  cp qmmm_jobs_single.xml qmmm_jobs.xml
  rm state.hdf5
  xtp_map -v -t system.data -c traj1.dump -s OPTIONS/mapping.xml -f state.hdf5 -i ${ITER}
  xtp_parallel -e qmmm -o OPTIONS/qmmm.xml -f state.hdf5 -j "run" -x 26
done
