import os
import json
import cloud_utils

def describe_environment():
    return {
        "region": os.environ.get("aws_default_region", "region"),
        "profile": os.environ.get("AWS_PROFILE", "default"),
        "timestamp": cloud_utils.get_time_stamp()  
    }

if __name__ == "__main__":
    result = describe_environment()
    print(json.dumps(result, indent=2))