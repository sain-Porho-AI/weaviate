import weaviate
from weaviate.connect import ConnectionParams
import os

client = weaviate.WeaviateClient(
    connection_params=ConnectionParams.from_params(
        http_host="localhost",
        http_port="8099",
        http_secure=False,
        grpc_host="localhost",
        grpc_port="50052",
        grpc_secure=False,
    ),
    auth_client_secret=weaviate.auth.AuthApiKey("secr3tk3y"),
    additional_headers={
        "X-GOOGLE-Api-Key": os.getenv("GOOGLE_API_KEY")
    },
    additional_config=weaviate.config.AdditionalConfig(
        startup_period=10,
        timeout=(5, 15)  # Values in seconds
    ),
)

client.connect()  # When directly instantiating, you need to connect manually