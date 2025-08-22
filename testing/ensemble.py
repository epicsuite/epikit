import epikit
import os

# initialize ensemble
ensemble = epikit.ensemble("testing/data/ensemble.yaml")

os.makedirs('testing/scratch', exist_ok=True)
ensemble.write("testing/scratch/ensemble.yaml")

ensemble.create_ensemble_metadata("testing/scratch/ensemble")
