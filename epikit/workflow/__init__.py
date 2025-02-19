import epikit
import csv
import yaml

class workflow():

    def __init__(self, infile="workflow_init.yaml", rootdir=",", description=None, experiment=None, cellline=None, replicate=0, timeunits='hrs', timevalues=[], treatments=[], resolution=100000):

        # set defaults 
        self.cellline    = cellline 
        self.description = description
        self.experiment  = experiment 
        self.replicate   = replicate 
        self.resolution  = resolution
        self.rootdir     = rootdir
        self.timeunits   = timeunits
        self.timevalues  = timevalues
        self.treatments  = treatments 
        self.version     = epikit.__version__

        # load data, if present
        with open(self.rootdir + "/" + infile, 'r') as initdata:
            data = yaml.safe_load(initdata)

        if data:
            for key, value in data.items():
                setattr(self, key, value)

    def __str__(self):
        return f"cellline: {self.cellline}\ndescription: {self.description}\nexperiment: {self.experiment}\nreplicate: {self.replicate}\nresolution: {self.resolution}\nrootdir: {self.rootdir}\ntimeunits: {self.timeunits}\ntimevalues: {self.timevalues}\ntreatments: {self.treatments}\nversion: {self.version}" 

    def add_experimental_design(self):
        self.datasets = [] 
        with open(self.rootdir + "/experimental_design.csv") as ed:
            edfile = csv.DictReader(ed, delimiter=',')
            self.datasets.append([])
            self.datasets.append([])
            for row in edfile:
                self.datasets[0].append(row['filename_0'])
                self.datasets[1].append(row['filename_1'])
