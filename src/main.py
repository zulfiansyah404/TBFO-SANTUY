import sys, argparse
from proccess.token import create_token
from proccess.CFGtoCNF import mapCNF, convertCFG, readFile, writeCNF



if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument('file', type = argparse.FileType('r'))
    # args = parser.parse_args()
    
    
    
    # Membuat splash screen dari banner/splash.txt
    splash = open("src/banner/splash.txt", "r")
    print(splash.read())
    
    # token = create_token(args.file.name)
    # token = [var.lower() for var in token]
    CNF = mapCNF(convertCFG(readFile('bin/cfg.txt')))
    writeCNF(convertCFG(readFile('bin/cfg.txt')))
    print(CNF)
    # parser(token, CNF)

    # print(token)
