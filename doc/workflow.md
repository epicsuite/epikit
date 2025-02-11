# EPIC workflow

| Step             | Inputs     | Outputs |
| ---------------- | --------   | ------- |
| FastQ to HiC     | FastQ file | HiC file | 
| HiC to Structure | HiC file   | structure.csv per chromosome in HiC file |
| Vis Data Fusion  | structure.csv   | filename.vtp (2) |
|                  | tracks.csv  (n) |  | 
|                  | session.yaml    |  | 
| Interactive Vis  | session.yaml     | interactive visualization | 
|                  | filename.vtp (2) | screen.png (n) | 
|                  |                  |  session state file | 

