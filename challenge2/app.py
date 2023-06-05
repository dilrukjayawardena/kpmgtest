import requests
import json

def get_instance_metadata(key):
    headers = {'X-aws-ec2-metadata-token-ttl-seconds': '21600'}
    token=requests.put("http://169.254.169.254/latest/api/token",headers=headers)
    token_header= {"X-aws-ec2-metadata-token":token.text}
    response = requests.get(f"http://169.254.169.254/latest/meta-data/{key}", headers=token_header)
    if response.status_code==200:
        return response.text.split("\n")
    else:
        return f"failed with status code {response.status_code}"

def main():
    print('please enter key to be retrieved')
    key = str(input())
    value=get_instance_metadata(key)
    data={key:value}
    print(json.dumps(data))

if __name__ == "__main__":
    main()