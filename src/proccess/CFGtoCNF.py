import os

rules = {}

def readFile(file):
    with open(file) as File:
        grammar = File.readlines()
        grammarAsList = []
        for line in grammar:
            if line.startswith(('/', '#')):
                continue
            convertedLine = line.replace("->", '').split()
            grammarAsList.append(convertedLine)
    return grammarAsList

def addRule(rule):
    global rules

    if rule[0] not in rules:
        rules[rule[0]] = []
    rules[rule[0]].append(rule[1:])

def convertCFG(grammars):
    global rules

    CNF = []
    unitProductions = []

    for rule in grammars:
        newRules = []
        idx = 0
        if len(rule)==2 and not rule[1][0].islower():
            unitProductions.append(rule)
            addRule(rule)
        
        while len(rule)>3:
            while f"{rule}{idx}" in rules:
                idx += 1
            newRules.insert(0, [f"{rule[0]}{idx}", rule[1], rule[2]])
            rule = [rule[0]] + [f"{rule[0]}{idx}"] + rule[3:]
            idx += 1
        
        if rule:
            addRule(rule)
            CNF.append(rule)
        
        if newRules:
            for newRule in newRules:
                addRule(newRule)
                CNF.append(newRule)
        
    while unitProductions:
        rule = unitProductions.pop()
        if rule[1] in rules:
            for values in rules[rule[1]]:
                newRule = [rule[0]] + values
                if len(newRule) > 2 or newRule[1][0].islower():
                    CNF.append(newRule)
                else:
                    unitProductions.append(newRule)
                addRule(newRule)
    
    return CNF


def writeCNF(CNF):
    file = open(os.getcwd()+'\\bin\\cnf.txt', 'w')
    for rule in CNF:
        file.write(rule[0])
        file.write(" -> ")
        for var in rule[1:]:
            file.write(var)
            file.write(" ")
        file.write("\n")
    file.close()

def mapCNF(CNF):
    length = len(CNF)
    dict = {}
    for rule in CNF:
        dict[rule[0]] = []
        val = []
        for idx in range(1, len(rule)):
            val.append(rule[idx])
        dict[rule[0]].append(val)
    return dict