from dotenv import load_dotenv
import os

load_dotenv()

DATASTREAM_API_KEY = os.getenv(
    "DATASTREAM_API_KEY"
)