import os
import sys 
import re

def lex(text, tokenExprs):
    pos = 0             # absolute position
    currPos = 1         # position in relative to line
    line = 1            # current line
    tokens = []
    i = 0
    while (pos < len(text)):
        print("\n" ,pos, line, currPos, "\n")
        if text[pos] == '\n':
            line += 1
            currPos = 1

        flag = None
        for tokenExpr in tokenExprs:
            # print(tokenExpr)
            pattern, tag = tokenExpr    
            
            regex = re.compile(pattern) # create regex
            flag = regex.match(text, pos)   #

            if flag:
                # texts = flag.group(0)
                if tag:
                    print(tag)
                    token = tag
                    tokens.append(token)
                break

        if not flag:
            print(f"\nSYNTAX ERROR\nIllegal character {text[pos]} at line {line} and column {currPos}")
            sys.exit(1)
        else:
            pos = flag.end(0)
        currPos += 1
        print(tokens)

    return tokens

tokenExprs = [
    # Not token
    (r'[ \t]+',                                      None),
    (r'#[^\n]*',                                     None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),
    (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',             "MULTILINE"),
    (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',             "MULTILINE"),
    (r'\n',                                          None),

    # Logika
    (r'\=(?!\=)',       "EQUAL"),
    (r'\==',            "IS_EQUAL"),
    (r'\===',           "IS_EQUALS"),
    (r'\!=',            "IS_NOT_EQUAL"),
    (r'\!==',           "IS_NOT_EQUALS"),
    (r'\&&',            "AND"),
    (r'\|\|',           "OR"),
    (r'\!',             "NOT"),
    (r'<=',             "LE"),
    (r'<',              "L"),
    (r'>=',             "GE"),
    (r'>',              "G"),

    # Operator
    (r'-=',             "SUBEQ"),
    (r'\*=',            "MULTEQ"),
    (r'\+=',            "PLUSEQ"),
    (r'/=',             "DIVEQ"),
    (r'\->',            "ARROW"),
    (r'\+',             "ADD"),
    (r'\-',             "SUBTR"),
    (r'\*',             "MULT"),
    (r'/',              "DIV"),
    (r'\,',             "COMMA"),
    (r'\w+[.]\w+',      "DOTBETWEEN"),
    (r'\.',             "DOT"),
    (r'\%',             "MOD"),
    (r'\%=',            "MODEQ"),
    (r'\*\*',           "POWER"),
    (r'\+\+',           "INCRE"),
    (r'\--',            "DECRE"),

    # Type
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),

    # Variabel
    (r'\bconst\b',              "CONST"),
    (r'\bvar\b',                "VAR"),
    (r'\blet\b',                "LET"),
    (r'\bnull\b',               "NULL"),

    # keyword
    (r'\btrue\b',               "TRUE"),
    (r'\bfalse\b',              "FALSE"),
    (r'\bNone\b',               "NONE"),
    (r'\bif\b',                 "IF"),
    (r'\belse\b',               "ELSE"),
    
    (r'\bfor\b',                "FOR"),
    (r'\bwhile\b',              "WHILE"),
    (r'\bbreak\b',              "BREAK"),
    (r'\bcontinue\b',           "CONTINUE"),
    (r'\bfrom\b',               "FROM"),
    (r'\bimport\b',             "IMPORT"),
    (r'\bas\b',                 "AS"),
    (r'\bis\b',                 "IS"),
    (r'\bfunction\b',           "FUNC"),
    (r'\breturn\b',             "RETURN"),
    (r'\braise\b',              "RAISE"),
    (r'\bwith\b',               "WITH"),
    (r'\bclass\b',              "CLASS"),
    (r'\btry\b',                "TRY"),
    (r'\bexcept\b',             "EXCEPT"),
    (r'\bfinally\b',            "FINALLY"),
    (r'\bdefaut\b',             "DEFAULT"),

    (r'\bconst\b',              "CONST"),
    (r'\bdelete\b',             "DELETE"),
    (r'\bswitch\b',             "SWITCH"),
    (r'\bcase\b',               "CASE"),
    (r'\bthrow\b',              "THROW"),
    (r'\bcatch\b',              "CATCH"),
    (r'\bcontinue\b',           "CONTINUE"),

    # Key

    (r'\b\,\b',                 "COMMA"),
    (r'\b\.\b',                 "DOT"),
    (r'\b\:\b',                 "DOUBLE_DOT"),
    (r'\;',                     "SEMICOLON"),
    (r"\b\'\b",                 "QOUTATION"),
    (r'\b\"\b',                 "DOUBLE_QOUTATION"),
    (r'\(',                     "LPR"),
    (r'\)',                     "RPR"),
    (r'\{',                     "LCR"),
    (r'\}',                     "RCR"),

    # Exception for variable
    (r'[A-Za-z_][A-Za-z0-9_]*', "VARIABLE"),
  ]


def create_token(filename):
    # Read file
    file = open(filename, encoding="utf8")
    characters = file.read()
    file.close()
    print(characters)
    tokens = lex(characters, tokenExprs)
    tokenResult = []

    for token in tokens:
        tokenResult.append(token)


    # Write file
    return tokenResult

# if __name__ == "__main__": 
#     path = os.getcwd()
#     createToken(path + "/test/inputAcc.txt")
