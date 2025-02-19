import epikit
import csv
import yaml
import os

class workflow():

    def __init__(self, infile="workflow.init", cline=None, description=None, experiment=None, replicate=0, 
                 resolution=100000, rootdir=",", timeunits='hrs', timevalues=[], treatments=[], ):

        # set defaults 
        self.cline       = cline 
        self.description = description
        self.experiment  = experiment 
        self.replicate   = replicate 
        self.resolution  = resolution
        self.rootdir     = os.path.abspath(rootdir)
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

        self.add_experimental_design()

    def __str__(self):
        return f"cline: {self.cline}\ndescription: {self.description}\nexperiment: {self.experiment}\nreplicate: {self.replicate}\nresolution: {self.resolution}\nrootdir: {self.rootdir}\ntimeunits: {self.timeunits}\ntimevalues: {self.timevalues}\ntreatments: {self.treatments}\nversion: {self.version}\ndatasets: " + str(self.datasets)

    def add_experimental_design(self):
        self.datasets = [] 
        with open(self.rootdir + "/experimental_design.csv") as ed:
            # this reader will skip the first line of a csv file (the column names)
            edfile = csv.DictReader(ed, delimiter=',')
            self.datasets.append([])
            self.datasets.append([])
            for row in edfile:
                self.datasets[0].append(row['filename_0'])
                self.datasets[1].append(row['filename_1'])

    def write(self, dest):
        with open(dest, 'w') as file:
            yaml.dump(self.__dict__, file)
