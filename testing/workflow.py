import epikit
import os

workflow = epikit.workflow(rootdir="testing/data")

print(workflow)

os.makedirs('tmp', exist_ok=True)
workflow.write("tmp/workflow.yaml")
