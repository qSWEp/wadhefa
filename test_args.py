import argparse

parser = argparse.ArgumentParser(description="Test argparse")

parser.add_argument("title")
parser.add_argument("company")
parser.add_argument("status", choices=["applied" , "rejected" , "saved"])

args = parser.parse_args()

print(f"title - {args.title}  company - {args.company} status - [{args.status}]")

