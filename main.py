import subprocess

print("Starting Data Pipeline...")

print("Running Ingestion...")
subprocess.run(["python", "data_pipeline/ingest.py"], check=True)

print("Running Transformation...")
subprocess.run(["python", "data_pipeline/transform.py"], check=True)

print("Generating Metrics...")
subprocess.run(["python", "analytics/metrics.py"], check=True)

print("Pipeline Finished Successfully")
