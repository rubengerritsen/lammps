#!/bin/bash
mkdir -p /tmp/qmpackage/id
/opt/orca-4.2.1/orca system.inp > system.log
/opt/orca-4.2.1/orca_2mkl system -molden
