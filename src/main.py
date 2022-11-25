import sys, argparse
from proccess.token import createToken
from proccess.CFGtoCNF import *
from proccess.parser_proccess import parserr
from time import time


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type = argparse.FileType('r'))
    args = parser.parse_args()
    
    
    
    # Membuat splash screen dari banner/splash.txt
    splash = open("src/banner/splash.txt", "r")
    print(splash.read())
    splash.close()

    # Buat tampilan compiling
    start_time = time()
    print("\n=============================================")
    print("Compiling " + args.file.name + "...")
    print("")

    token = createToken(args.file.name)

    if (token != -1):
        token = [var.lower() for var in token]
        CNF = mapCNF(convertCFG(readFile('bin/cfg.txt'))   )
        #writeGrammar(convertGrammar(readGrammarFile('bin/cfg.txt')))
        # print(CNF)
        parserr(token, CNF)
    print("\nExecution Time : " + str(time() - start_time) + " seconds")
    print("=============================================")
    # print(token)
