import sys, argparse
from proccess.token import create_token
from proccess.CFGtoCNF import *
from proccess.parser_proccess import parserr


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type = argparse.FileType('r'))
    args = parser.parse_args()
    
    
    
    # Membuat splash screen dari banner/splash.txt
    splash = open("src/banner/splash.txt", "r")
    print(splash.read())
    
    token = create_token(args.file.name)
    token = [var.lower() for var in token]
    print(token)
    CNF = mapGrammar(convertGrammar(readGrammarFile('bin/cfg.txt'))   )
    writeGrammar(convertGrammar(readGrammarFile('bin/cfg.txt')))
    # print(CNF)
    parserr(token, CNF)

    # print(token)
