import pandas as pd
import json



def get_key(data,key):
    formatted_key=key.replace('/','.')
    df = pd.json_normalize(data)
    return df[formatted_key].values[0]




def main():
    try:
        print('please enter json')
        data = json.loads(input())
        print('please enter key')
        key = str(input())
        key_value=get_key(data,key)
        print(f'value is {str(key_value)}')
    except Exception as e:
        print(f'error occured:{str(e)}')
    finally:
        print('Done')

if __name__ == "__main__":
    main()
