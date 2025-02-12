import os

from dotenv import load_dotenv
from google.cloud import modelarmor_v1


load_dotenv()
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
TEMPLATE_ID = os.getenv("TEMPLATE_ID")

client = modelarmor_v1.ModelArmorClient(
    client_options={
        "api_endpoint": f"modelarmor.{LOCATION}.rep.googleapis.com",
    }
)
