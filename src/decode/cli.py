import argparse
import json
import boto3
from clint.textui import colored, puts


def decode_authorization_message(profile, region, message):
    """assume profile and decode autorization message with sts"""
    session = boto3.Session(profile_name=profile, region_name=region)
    sts = session.client('sts')
    return json.loads(sts.decode_authorization_message(EncodedMessage=message)["DecodedMessage"])


def main():
    parser = argparse.ArgumentParser(
        description=main.__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--profile", required=True, help=f"AWS CLI Profile")
    parser.add_argument("--message", required=True, help=f"Message to decode")
    parser.add_argument("--aws-region", help=f"AWS region", default="eu-west-1")
    try:
        args = parser.parse_args()
        print(json.dumps(decode_authorization_message(args.profile, args.aws_region, args.message), indent=2))

    except argparse.ArgumentError as exc:
        puts(colored.red(f"Error while parsing arguments: {exc}"))


if __name__ == '__main__':
    main()
