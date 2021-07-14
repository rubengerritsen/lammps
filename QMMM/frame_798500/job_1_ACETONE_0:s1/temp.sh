#!/bin/bash
mkdir -p /tmp/qmpackage/id
/opt/orca-4.2.1/orca temp.inp > temp.log
/opt/orca-4.2.1/orca_2mkl temp -molden
