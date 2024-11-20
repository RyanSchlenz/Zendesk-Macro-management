Zendesk Macro Management Scripts
This repository contains three Python scripts that interact with the Zendesk API to manage macros. The scripts allow you to:

Fetch and display all existing macros.
Create new macros.
Delete a macro by name.
Prerequisites
Before using these scripts, ensure you have the following prerequisites:

Python 3.x installed.
The following Python libraries:
requests (for making HTTP requests to the Zendesk API)
datetime (for managing timestamps)
You can install the required dependencies with:


pip install requests
Zendesk API Token: You will need an API token from your Zendesk account. This will be used for authentication.
Configuration
Before running the scripts, ensure you have configured your Zendesk subdomain and API token in a file named project_config.py.

Create a project_config.py file in the same directory as the scripts with the following content:


subdomain = "your_zendesk_subdomain"
api_token = "your_zendesk_api_token"
Replace your_zendesk_subdomain and your_zendesk_api_token with your actual Zendesk subdomain and API token.

Scripts Overview
1. Fetch All Macros
This script fetches and displays all existing macros from your Zendesk account. It outputs the macro title, creation date, and last updated date for each macro.



2. Create a New Macro
This script allows you to create a new macro with a specified name and actions (e.g., set a comment or ticket status). You need to specify the name and actions for the macro.


3. Delete a Macro by Name
This script deletes a macro based on its name. It first searches for the macro by its title and deletes it if found.



Example Usage:
Fetch All Macros:

Run fetch_macros.py to list all your macros in Zendesk.
The output will show the title, created date, and updated date of each macro.


Create a New Macro:

Run create_macro.py to create a macro.
Modify the macro's name and actions to suit your needs. For example:
Set the comment_value field to a custom message.
Set the status field to "solved."

Delete a Macro by Name:

Run delete_macro.py and provide the name of the macro you want to delete.
The script will attempt to find the macro by name and delete it.
Example: Create a Macro
Here’s an example of how the macro creation works:

# Creating a macro with custom actions
macro_name = "Example Macro"
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

create_macro(macro_name, macro_actions)
This script will create a macro titled Example Macro with actions to set a comment value and mark the ticket as "solved."

Troubleshooting
Failed API Request: If any request fails (e.g., incorrect API token, issues with the network), ensure that your API token and subdomain are correctly configured in project_config.py.

Macro Not Found: If the macro you want to delete isn’t found, ensure the name is correctly spelled and that the macro exists in your Zendesk account.

Contributing
If you have improvements or new features to add, feel free to fork the repository and submit a pull request.

License
This project is licensed under the MIT License.