import os
from typing import Optional

from bitwarden_sdk import BitwardenClient, client_settings_from_dict, DeviceType
from dotenv import load_dotenv


def get_bw_client(token_name: Optional[str] = None) -> BitwardenClient:
    if token_name is None:
        token_name = "BW_CLIENT_TOKEN"
    load_dotenv()

    client = BitwardenClient(
        client_settings_from_dict({
            "identity_url": "https://identity.bitwarden.com",
            "api_url": "https://api.bitwarden.com",
            "user_agent": "Python",
            "device_type": DeviceType.SDK
        })
    )
    client.auth().login_access_token(os.getenv(token_name), "state.json")

    return client
