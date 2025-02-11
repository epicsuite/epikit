# EPIC workflow

| Step             | Inputs     | Outputs |
| ---------------- | --------   | ------- |
| FastQ to HiC     | FastQ file | HiC file | 
| HiC to Structure | HiC file   | structure.csv per chromosome in HiC file |
| Vis Data Fusion  | structure.csv (num timesteps)   | filename.vtp (one per time step) |
|                  | tracks.csv  (n x num timesteps) |  | 
| Interactive Vis  | session.yaml     | interactive visualization | 
|                  | filename.vtp (2) | screen.png (n) | 
|                  |                  |  session state file | 

