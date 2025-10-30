import logging, pandas as pd

logging.basicConfig(level=logging.INFO)
logging.info("Script started")
logging.warning("Missing value encountered")

# Error Handling with try/except:
try:
    price = float("prueba")
except ValueError:
    logging.error("Failed to convert price")

# Combine both:
try:
    df = pd.read_csv("/home/adminuser/AyscomAcademy/scriptlesson/backup")
except FileNotFoundError:
    logging.error("File not found")
    exit(1)
