import csv
import yaml

class workflow():

    def __init__(self, input="workflow_input.yaml", rootdir=",", description=None, experiment=None, cellline=None, replicate=0, timeunits='hrs', timevalues=[], resolution=100000):
        self.rootdir     = rootdir
        with open(init, 'r') as initdata:

        self.description = description
        self.experiment  = experiment 
        self.cellline    = cellline 
        self.replicate   = replicate 
        self.timeunits    = timeunits
        self.timevalues  = timevalues
        self.resolution  = resolution

    def add_experimental_design(self):
        self.datasets = [] 
        with open(self.rootdir + "/experimental_design.csv") as ed:
            edfile = csv.DictReader(ed, delimiter=',')
            self.datasets.append([])
            self.datasets.append([])
            for row in edfile:
                self.datasets[0].append(row['filename_0'])
                self.datasets[1].append(row['filename_1'])
        print(self.datasets)
