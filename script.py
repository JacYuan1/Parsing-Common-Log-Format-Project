from pathlib import Path
import json
target = Path.home() / "Desktop" / "Coding Projects" / "Python Folder" / ".vscode" / "Lab8" / "final.json" # Change this to the path of your json file

with target.open("r") as f:
    data = json.load(f)

usr_input = input("Please enter a field of your choice: 1) IP_of_requesting_host 2) Remote_user 3) Remote_user 4) Request_from_client 5) HTTP_response_code 6) Size_of_bytes_returned 7) Http_referer 8) Http_user_agent: ")
final_str = ""
for x in data:
    for key in x.items():
        if usr_input == key[0]:
            final_str = final_str + ", " + key[1]

print("\nAll the results of the field " + usr_input + ": " + final_str[2:])