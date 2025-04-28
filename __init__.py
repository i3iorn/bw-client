import os

from bitwarden_sdk import BitwardenClient, client_settings_from_dict, DeviceType
from dotenv import load_dotenv


def get_bw_client():
    load_dotenv()

    client = BitwardenClient(
        client_settings_from_dict({
            "identity_url": "https://identity.bitwarden.com",
            "api_url": "https://api.bitwarden.com",
            "user_agent": "Python",
            "device_type": DeviceType.SDK
        })
    )
    client.auth().login_access_token(os.getenv("TOKEN"), "state.json")

    return client
