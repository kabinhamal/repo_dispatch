import hcl2
import json

# JSON input
json_str = '{"asg5": {"env": "dev","managed_asg": true,"instance": "003","location": "EASTUS","purpose": "test","additional_tags": {}}}'

# Parse JSON into Python dict
json_dict = json.loads(json_str)

# Convert Python dict to HCL string
hcl_str = hcl2.dumps(json_dict)

print(hcl_str)
