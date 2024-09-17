

Input data are processed into a data hierarchy that organizes collections of structure
and data files. Structure files define 3D geometry for a specific collection of genomic
material. Data can then be mapped into 3D space by using a specific structure.

## Input datasets

```
artifact/
    meta.yaml
    structure/
        chr1/
            100000/
                structure.csv
                meta.yaml
            250000/
                structure.csv
                meta.yaml
        chr10/
            100000/
                structure.csv
                meta.yaml
            250000/
                structure.csv
                meta.yaml
    data/
        peak/
            0/
                data.csv 
                meta.yaml
            1/
                data.csv 
                meta.yaml
        feature/
        track/
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

## Comparative visualization

This includes enough information to view two artifacts with the same definition of a
sequence.
