import epikit

workflow = epikit.workflow(rootdir="testing/data")
workflow.add_experimental_design()

print(workflow)
