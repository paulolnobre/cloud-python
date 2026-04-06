def format_bucket_name(project, environment, region):
    return f"{project}-{environment}-{region}"

def validate_environment(env):
    if env == "dev" or env == "staging" or env == "prod":
        return True
    else: 
        return False
    
def build_lambda_arn(region, account_id, function_name):
    return f"arn:aws:lambda:{region}:{account_id}:function:{function_name}"

def main():
    bucket_name = format_bucket_name("myproject", "prod", "us-west-1")
    print(bucket_name)
    # optional: validate env and print result
    print("Environment valid:", validate_environment("prod"))
    print("Environment valid:", validate_environment("invalid"))
    arn = build_lambda_arn("us-west-1", "123456789012", "my_lambda_function")
    print(arn)



if __name__ == "__main__":
    main()
   