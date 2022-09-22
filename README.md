# decode-authorization-message

A CLI tool to decode AWS authorization messages

## Features

### decode-authorization-message 

- decode the message when there is an authorization failure and return JSON formated response

## License

- see [license file](./LICENSE.txt)

## References

- [AWS API Documentation](https://docs.aws.amazon.com/STS/latest/APIReference/API_DecodeAuthorizationMessage.html)

## Setup

### Requirements

- [pipx](https://pypa.github.io/pipx/)

### Installation

- Run the following command

````shell
pipx install git+https://github.com/tsenay/decode-authorization-message.git
````

### Upgrade

````shell
pipx upgrade decode-authorization-message
````

### Reinstall

````shell
pipx install git+https://github.com/tsenay/decode-authorization-message.git --force
````

## Usage

### decode-authorization-message

- Type the following command to list available options : 

````shell
decode-authorization-message --help
````

Example:

```
usage: decode-authorization-message [-h] --profile PROFILE --message MESSAGE [--aws-region AWS_REGION]

options:
  -h, --help            show this help message and exit
  --profile PROFILE     AWS CLI Profile
  --message MESSAGE     Message to decode
  --aws-region AWS_REGION
                        AWS region
```


## Example

````shell
decode-authorization-message --profile my_account.my_profile --message 'Qe68ediGX...8Ie7-MYRA' --aws-region eu-west-1 | jq '.'
````

## Contributing


- Feel free to create a PR for improvement and/or fixes
