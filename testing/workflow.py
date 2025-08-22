import epikit
import os

inputdeck = epikit.inputdeck("testing/data/workflow.yaml")

os.makedirs('testing/scratch', exist_ok=True)
inputdeck.write("testing/scratch/workflow.yaml")

inputdeck.create_ensemble_metadata("testing/scratch/ensemble")
