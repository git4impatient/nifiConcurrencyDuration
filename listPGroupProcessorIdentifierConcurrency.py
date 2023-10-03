# (c) copyright 2023 Martin Lurie - sample code not supported

import json

# Load the provided JSON data
with open('input.json', 'r') as input_file:
    data = json.load(input_file)

# Initialize a list to store the extracted information
extracted_data = []

# Extract the information from the JSON structure
for process_group in data['flowContents']['processGroups']:
    for processor in process_group['processors']:
        extracted_data.append({
            'processGroup': process_group['name'],
            'processor': processor['name'],
            'instanceIdentifier': processor['instanceIdentifier'],
            'concurrentlySchedulableTaskCount': processor['concurrentlySchedulableTaskCount'],
            'runDurationMillis': processor['runDurationMillis']
        })

# Create a new JSON file with the extracted data
with open('output.json', 'w') as output_file:
    json.dump(extracted_data, output_file, indent=2)

print("Data extraction and JSON creation completed.")

