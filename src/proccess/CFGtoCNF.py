rules = {}

def readFile(file):
  with open(file) as CFG:
    CNF = CFG.readlines()
    cfgAsList = []
    for i in range(len(CNF)):
      splitBaris = CNF[i].replace("->", "").split()
      cfgAsList.append(splitBaris)
  return cfgAsList

def addRule(rule):
  global rules
  
  if rule[0] not in rules:
    rules[rule[0]] = []
  rules[rule[0]].append(rule[1:])

def convertCFG(CFG):
    global rules

    CNF = []
    unitProductions = []
    idx = 0
    
    for rule in CFG:
      newRules = []
      if len(rule) == 2 and not rule[1][0].islower() :
        unitProductions.append(rule)
        addRule(rule)
        continue
      while len(rule) > 3:
        newRules.append([f"{rule[0]}{idx}", rule[1], rule[2]])
        rule = [rule[0]] + [f"{rule[0]}{idx}"] + rule[3:]
        idx += 1

      if rule:
        addRule(rule)
        CNF.append(rule)
      if newRules:
        for i in range(len(newRules)):
          CNF.append(newRules[i])

    while unitProductions:
      rule = unitProductions.pop() 
      if rule[1] in rules:
        for item in rules[rule[1]]:
          newRules = [rule[0]] + item
          if len(newRules) > 2 or newRules[1][0].islower():
            CNF.append(newRules)
          else:
            unitProductions.append(newRules)
          addRule(newRules)
    return CNF

def mapCNF(CNF):
  mp = {}
  for rule in CNF :
    mp[str(rule[0])] = []
  for rule in CNF :
    elm = []
    for idxRule in range(1, len(rule)) :
      apd = rule[idxRule]
      elm.append(apd)
    mp[str(rule[0])].append(elm)
  return mp

def writeCNF(CNF):
    file = open('bin/cnf.txt', 'w')
    for rule in CNF:
        file.write(rule[0])
        file.write(" -> ")
        for i in rule[1:]:
            file.write(i)
            file.write(" ")
        file.write("\n")
    file.close()

# if __name__ == "__main__":
writeCNF(convertCFG((readFile("bin/cfg.txt")))) 