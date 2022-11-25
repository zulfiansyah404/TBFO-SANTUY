def parserr(token, CNF):
    tokenLength = len(token)
    cyk = [[set([]) for j in range(tokenLength)] for i in range(tokenLength)]
    for i in range(tokenLength):
        for key, value in CNF.items():
            for rule in value:
                if len(rule) == 1 and rule[0] == token[i]:
                    cyk[i][i].add(key)

        for j in range(i, -1, -1):
            for k in range(j, i):
                for key, value in CNF.items():
                    for rule in value:
                        if (len(rule) == 2) and (rule[0] in cyk[j][k]) and (rule[1] in cyk[k+1][i]):
                            cyk[j][i].add(key)

    print(cyk[0])   
    if ('S') in cyk[0][tokenLength-1]:
        print("Accepted")
    else:
        print("Syntax Error")