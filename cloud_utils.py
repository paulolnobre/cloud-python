from datetime import datetime 

def get_resource_name(service, env, region):
    return f"{service}-{env}-{region}"

def format_s3_size(b):
    KB = 1024
    MB = 1048576
    GB = 1073741824
    TB = 1099511627776
    if b < KB:
        return f"{b}B"
    elif KB < b < MB:
        return f"{round(b/KB)}KB"
    elif MB < b < GB:
        return f"{round(b/MB)}MB"
    elif GB < b < TB:
        return f"{round(b/GB)}GB"
    elif b > TB:
        return f"{round(b/TB)}TB"
    else:
        return "invalid"


def get_time_stamp():
    return datetime.now().strftime("%Y-%m-%d")

if __name__ == "__main__":
    print(get_resource_name("s3", "prod", "us-east-1"))
    print(format_s3_size(1105548))
    print(get_time_stamp())


   