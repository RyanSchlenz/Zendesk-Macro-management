import requests
from requests.auth import HTTPBasicAuth
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import from project_config
from project_config import email, subdomain, api_token


# Authentication setup using HTTPBasicAuth
auth = HTTPBasicAuth(f"{email}/token", api_token)

# Headers for API requests
headers = {
    "Content-Type": "application/json"
}

# Function to create a new macro using authenticated API request
def create_macro(name, actions):
    url = f'https://{subdomain}.zendesk.com/api/v2/macros.json'
    data = {
        "macro": {
            "title": name,
            "actions": actions
        }
    }
    response = requests.post(url, json=data, headers=headers, auth=auth)
    if response.status_code == 201:
        print(f"Macro '{name}' created successfully!")
        return True
    else:
        print(f"Failed to create macro. Status code: {response.status_code}, Error: {response.text}")
        return False

# Example usage
if __name__ == "__main__":
    macro_name = "Example Macro11"
    macro_actions = [
        {
            "field": "comment_value",
            "value": "Thank you for contacting us! We'll get back to you shortly."
        },
        {
            "field": "status",
            "value": "solved"
        }
    ]
    
    success = create_macro(macro_name, macro_actions)
    if success:
        print("Macro creation successful!")
    else:
        print("Macro creation failed!")
