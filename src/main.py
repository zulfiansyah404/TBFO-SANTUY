import sys, argparse
from proccess.token import create_token

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type = argparse.FileType('r'))
    args = parser.parse_args()
    
    token = create_token(args.file.name)
    
    print(token)
