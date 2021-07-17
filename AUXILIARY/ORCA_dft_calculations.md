# Create Input Files with ORCA
### ! All ORCA calculations are already performed. The results are in `DFT_ORCA`.
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

### Next use CHELPG to do a charge fit and calculate the molecular polarizability
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
See the input files in `DFT_ORCA`.
