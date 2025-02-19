import epikit

workflow = epikit.workflow(rootdir="testing/data")

print(workflow)

workflow.write()
