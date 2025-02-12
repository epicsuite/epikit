# EPIC workflow

## directory structure and example files
```
(unique identifier)/
   experiment.csv
   workflow.yaml
   build/
     fastq/
       filename1.fastq
       filename2.fastq
       ...
       filename3.fastq
     0.0.hic
     0.1.hic
     ...
     1.n.hic
   results/
```

# workflow definition file

`workflow.yaml`
```
version: x.x
experiment: name
datasets:
  replicate: 1
  timeunits: hr
  timevalues: [24, 48]
  resolution: 100000
  0:
    treatment: name
    files:
      fastq:
        - /path/to/file.fastq
        - /path/to/file.fastq
        - /path/to/file.fastq
  1:
    treatment: name
      fastq:
        - /path/to/file.fastq
        - /path/to/file.fastq
        - /path/to/file.fastq
```

## HiC to Structure step

hic-to-structure.yaml
```
```

