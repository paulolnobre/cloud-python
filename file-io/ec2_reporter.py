import json
from datetime import datetime


def load_aws_config(filepath):
    """
    Reads an AWS JSON config file and returns it as a dictionary.
    """
    # TODO: use "with open" with mode "r" to open the file
    # use json.load() to convert the content into a dictionary
    # return the dictionary
    with open(filepath, "r") as f:
        return json.load(f)
  

def load_ec2_instances(filepath):
    """
    Reads a JSON file containing a list of EC2 instances.
    """
    # TODO: same structure as load_aws_config
    # return the list of instances
    with open(filepath, "r") as f:
        return json.load(f)


def filter_instances_by_state(instances, state):
    """
    Filters instances by state: "running" or "stopped".
    """
    # TODO: use a list comprehension to return only
    # instances where instance["state"] == state
    return [instance for instance in instances if instance["state"] == state]


def write_text_report(instances, config, filepath):
    """
    Writes a .txt report summarizing the EC2 instances.
    """
    timestamp = datetime.now().isoformat()

    # TODO: use "with open" with mode "w" to open the file
    # Write the following lines:
    # line 1: "=== AWS EC2 Report ===\n"
    # line 2: f"Project: {config['project']} | Env: {config['environment']} | Region: {config['region']}\n"
    # line 3: f"Generated: {timestamp}\n"
    # line 4: "\n"
    # then iterate over instances and for each one write:
    # f"  [{instance['state'].upper()}] {instance['name']} ({instance['id']}) - {instance['type']}\n"
    with open(filepath, "w") as f:
        f.write("=== AWS EC2 Report ===\n")
        f.write(f"Project: {config['project']} | Env: {config['environment']} | Region: {config['region']}\n")
        f.write(f"Generated: {timestamp}\n")
        f.write("\n")
        for instance in instances:
            f.write(f"  [{instance['state'].upper()}] {instance['name']} ({instance['id']}) - {instance['type']}\n")


def write_json_report(instances, config, filepath):
    """
    Writes a structured .json report — suitable for ingestion
    by other systems or storage in S3.
    """
    report = {
        "generated_at": datetime.now().isoformat(),
        "project": config["project"],
        "environment": config["environment"],
        "region": config["region"],
        "summary": {
            "total": len(instances),
            # TODO: use len() + filter_instances_by_state to count running
            "running": len(filter_instances_by_state(instances, "running")),    # TODO,
            # TODO: same logic for stopped
            "stopped": len(filter_instances_by_state(instances, "stopped"))  # TODO
        },
        "instances": instances
    }

    # TODO: use "with open" with mode "w" and json.dump() with indent=2
    # to save the report to filepath
    with open(filepath, "w") as f:
        json.dump(report, f, indent=2)


if __name__ == "__main__":
    # 1. Load configuration
    config = load_aws_config("aws_config.json")
    print(f"Config loaded: {config['project']} / {config['environment']} / {config['region']}")

    # 2. Load instances
    instances = load_ec2_instances("ec2_instances.json")
    print(f"Instances loaded: {len(instances)} total")

    # 3. Filter by state
    running = filter_instances_by_state(instances, "running")
    stopped = filter_instances_by_state(instances, "stopped")
    print(f"  Running: {len(running)} | Stopped: {len(stopped)}")

    # 4. Generate .txt report
    write_text_report(instances, config, "ec2_report.txt")
    print("TXT report generated: ec2_report.txt")

    # 5. Generate .json report
    write_json_report(instances, config, "ec2_report.json")
    print("JSON report generated: ec2_report.json")
