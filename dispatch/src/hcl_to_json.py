import json
import subprocess

hcl_payload = '''
asg5 = {
    env             = "dev" 
    managed_asg     = true
    instance        = "003"
    location        = "EASTUS"
    purpose         = "test"
    additional_tags = {}
}
'''

# Convert HCL to JSON using the hcl2json library
json_payload = subprocess.check_output(['hcl2json'], input=hcl_payload.encode()).decode()

# Parse the JSON payload
data = {
    'INPUT_PARAMETERS_JSON': json.loads(json_payload)
}

print(data)
