import os
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import sys

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import from project_config
from project_config import email, subdomain, api_token, LOG_FILE_PATH

# Authentication setup using HTTPBasicAuth
auth = HTTPBasicAuth(f"{email}/token", api_token)

# Headers for API requests
headers = {
    "Content-Type": "application/json"
}

# Function to fetch all macros using authenticated API request
def fetch_all_macros():
    try:
        url = f'https://{subdomain}.zendesk.com/api/v2/macros.json'
        response = requests.get(url, headers=headers, auth=auth)
        response.raise_for_status()  # Raise an error for non-200 status codes
        macros = response.json()['macros']
        return macros
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch macros: {e}")
        return None

# Function to prepend current macros to the top of the log file
def prepend_current_macros_to_log():
    current_macros = fetch_all_macros()
    if current_macros is not None:
        num_macros = len(current_macros)
        log_messages = [f"Script last ran at: {datetime.now()}"]  # Add the date and time the script last ran
        log_messages.append("")  # Add a space before listing the current macros
        log_messages.append(f"Current Macros ({num_macros}):")
        for macro in current_macros:
            log_messages.append(f"Title: {macro['raw_title']}")
            log_messages.append(f"Created At: {macro['created_at']}")
            log_messages.append(f"Updated At: {macro['updated_at']}")
            log_messages.append("")  # Add an empty line between each macro
        
        try:
            # Check if log file exists
            if not os.path.exists(LOG_FILE_PATH):
                print("Log file does not exist. Creating...")
                with open(LOG_FILE_PATH, 'w') as log_file:
                    log_file.write('Macro Activity Log\n\n')
                print("Log file created successfully.")

            # Read existing content of the log file
            with open(LOG_FILE_PATH, 'r') as log_file:
                existing_content = log_file.read()

            # Write updated content back to the file
            with open(LOG_FILE_PATH, 'w') as log_file:
                log_file.write('\n'.join(log_messages))
                log_file.write('\n\n')  # Add a new line after the current macros
                log_file.write(existing_content)
                
            print("Current macros prepended to log file.")
        except Exception as e:
            print(f"Error prepending current macros to log file: {e}")
    else:
        print("Failed to fetch current macros.")

# Example usage
if __name__ == "__main__":
    # Prepend all current macros to the top of the log file
    prepend_current_macros_to_log()
