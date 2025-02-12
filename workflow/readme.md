# EPIC workflow

## directory structure and example files
```
(unique identifier)/
   experiment.csv               table encoding the experimental design information for this workflow
   workflow.yaml
   hic-to-structure.yaml
   build/
     fastq/
       filename1.1.fastq
       filename1.2.fastq
       ...
       filename2.N.fastq
     0.0.hic
     0.1.hic
     ...
     1.n.hic
   results/
     chr1/
     chr2/
     ...
     chrN/
       vis-data-fusion.yaml
       session.yaml
       d0/
         0.vtp
         1.vtp
         ...
         n.vtp
       d1/
         0.vtp
         1.vtip
         ...
         n.vtip
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
          - /path/to/filename1.1.fastq
          - /path/to/filename1.2.fastq
          - ...
          - /path/to/filename1.N.fastq
  1:
    treatment: name
      fastq:
        - /path/to/filename2.1.fastq
        - /path/to/filename2.2.fastq
        - ...
        - /path/to/filename2.N.fastq
```

## HiC to Structure step

For each `fastq` file in the `workflow.yaml` file, produce a structure file in `build/chrN/(dataset)/(timestep)`

`hic-to-structure.yaml`

```
version: x.x
```

source directory: `build/`
destination directory: `build/chrN`

## Data upload step

Track data for a specific chromosome is added to the correct chromosome build directory. Files to be uploaded:

```
features.csv
track1.csv
track2.csv
...
trackN.csv
```

## Vis Data Fusion step

For a specific Chromosome, take the files in the `build` directory and create data in the `results` directory. This is done by iterating over the datasets and timesteps in the source directory and creating the correct number of files in the `results` directory.

`vis-data-fusion.yaml`

```
version: x.x
chromosome: N
tracks:
  peak:
    track1.csv
    track2.csv
    ...
  structure:
    track3.csv
    ...
    trackN.csv
```

Data source directory: `build/chrN/(dataset)/(timestep)`
