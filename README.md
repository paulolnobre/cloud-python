# cloud-python

Python scripts for AWS Cloud Engineering and infrastructure automation.

Built as a learning portfolio targeting AWS Solutions Architect Associate (SAA-C03) and entry-level Cloud Engineering roles.

## Structure

| Folder | Concept | Description |
|--------|---------|-------------|
| aws_naming | Functions | Reusable helpers for AWS resource naming conventions |
| ec2-audit | Lists & Loops | Filtering and auditing EC2 instances by state and type |
| ec2-cost-report | Dictionaries | Cost estimation based on EC2 instance types |
| error_handler | Error Handling | Simulating and handling AWS API errors with try/except |
| file-io | File I/O | Reading JSON configs and generating EC2 instance reports |

## Stack

- Python 3.13
- AWS boto3 (Stage 2+)
- AWS Free Tier

## Goal

Each folder is a standalone script covering a core Python concept applied to a real AWS use case.
The progression follows a structured path from Python fundamentals to full AWS automation and serverless deployment.

## Roadmap

- Stage 1 — Core Python for Cloud Scripting (in progress)
- Stage 2 — AWS Automation with boto3
- Stage 3 — Serverless and Lambda
- Stage 4 — AI Agents on AWS
- Stage 5 — CI/CD and Infrastructure as Code
