## Overview

Input data are processed into a data hierarchy that organizes collections of structure
and data files. Structure files define 3D geometry for a specific collection of genomic
material. Data can then be mapped into 3D space by using a specific structure.

## Input datasets

```
artifact/
    meta.yaml
    chr1/
        0/
            meta.yaml
            structure.csv
            peak/
                <name>/
                    data.csv 
                    meta.yaml
                <name>/
                    data.csv 
                    meta.yaml
            feature/
                <name>/
                    data.csv
                    meta.yaml
            track/
                <name>/
                    data.csv
                    meta.yaml
    chr<n>/
```

## 4D fused datasets

These datasets contain enough information to be viewed in 4D (3D plus some definition of
a sequence). 

```
artifact/
    meta.yaml
    0/
        meta.yaml
        structure.csv
        peak/
            0/
                data.csv
                meta.yaml
        feature/
            0/
                data.csv
                meta.yaml
    1/
        meta.yaml
        structure.csv
        peak/
            0/
                data.csv
                meta.yaml
        feature/
            0/
                data.csv
                meta.yaml
```

## Session 

This includes enough information to view two artifacts with the same definition of a
sequence.

```
session/
    session.yaml
```
