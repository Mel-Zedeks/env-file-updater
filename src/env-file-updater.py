import re
import os
# Function to update the value of multiple keys in a file


# def update_values(file_name, data,separator='='):
# # Get the current working directory
# cwd = os.path().basename()
# print(cwd)
# # Construct the full path to the file
# full_path = os.path.join(cwd, file_name)
# Open the file in read mode
with open(file_name, 'r') as file:
    # Read the contents of the file
    file_data = file.read()

for key, new_value in data.items():
    # Use regular expressions to search for the key
    match = re.search(key + ".*", file_data)
    if match:
        # Get the current value of the key
        current_value = match.group()
        # Update the value of the key
        updated_value = current_value.replace(
            current_value, key + separator + new_value)
        # Replace the current value of the key with the updated value
        file_data = file_data.replace(current_value, updated_value)
    else:
        print(f"{key} not found in the file")

# Open the file in write mode
with open(file_name, 'w') as file:
    # Write the updated contents to the file
    file.write(file_data)
    print("Update completed")