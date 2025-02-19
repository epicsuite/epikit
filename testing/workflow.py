import epikit
import os

workflow = epikit.workflow(rootdir="testing/data")
os.makedirs('testing/scratch', exist_ok=True)
workflow.write("testing/scratch/workflow.yaml")
