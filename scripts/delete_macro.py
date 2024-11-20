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

# Function to fetch all macros using authenticated API request
def fetch_all_macros():
    url = f'https://{subdomain}.zendesk.com/api/v2/macros.json'
    response = requests.get(url, headers=headers, auth=auth)
    response.raise_for_status()  # Raise an error for non-200 status codes
    macros = response.json()['macros']
    return macros

# Function to find macro by name
def find_macro_by_name(name):
    macros = fetch_all_macros()
    for macro in macros:
        if macro['title'] == name:
            return macro
    return None

# Function to delete macro by name
def delete_macro_by_name(name):
    macro = find_macro_by_name(name)
    if macro:
        macro_id = macro['id']
        url = f'https://{subdomain}.zendesk.com/api/v2/macros/{macro_id}.json'
        response = requests.delete(url, headers=headers, auth=auth)
        if response.status_code == 204:
            print(f"Macro '{name}' deleted successfully!")
        else:
            print(f"Failed to delete macro '{name}'. Status code: {response.status_code}, Error: {response.text}")
    else:
        print(f"Macro '{name}' not found.")

# Example usage
if __name__ == "__main__":
    macro_name = "Example Macro11"  # Change this to the name of the macro you want to delete
    delete_macro_by_name(macro_name)
