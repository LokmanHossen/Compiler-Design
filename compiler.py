#hemel sharker akash 170116

import re, os


class SymbolTable:
    headers = [
        "stdio.h",
        "math.h",
        "conio.h",
        "stdlib.h",
        "string.h",
        "ctype.h",
        "time.h",
        "float.h",
        "limits.h",
        "wctype.h"
    ]

    Keywords = [
        "int",
        "int64",
        "float",
        "double",
        "char",
        "if",
        "while",
        "goto",
        "for"
    ]
    
    AOperator = [
        "+",
        "-",
        "*",
        "="
    ]

    IOperator = [
        "++",
        "--"
    ]

    LOperator = [
        "&&",
        "||",
        "!=",
        "==",
        "<",
        ">",
        "<=",
        ">=",
    ]

    Punctuation = [
        "(",
        ")",
        "[",
        "]",
        ",",
        ";",
        "\"",
        "'",
        "{",
        "}",
        "#"
    ]

class ContextFreeGrammar:
    Identifier = f"([a-z]|_)([a-z]|_|\d)*"
    IdentifierType = f"(int|int64|float|double|char)"
    Space = f"\s*"
    SpNew = f"({Space}\\n*)*"
    Equal = f"({Space}={Space})"
    ArithmaticOperator = f"({Space}(\+|-|\*|\\\){Space})"
    Identifier_Digit = f"({Identifier}|\d+)"
    VariableTypeValue = f"({Identifier}(|({Equal}{Identifier_Digit}(|({ArithmaticOperator}{Identifier_Digit})*))))"

    VariableDeclarationLine = f"({SpNew}{IdentifierType}{Space}{VariableTypeValue}(,{SpNew}{VariableTypeValue}{SpNew})*{SpNew})"
    VariableDeclarationFor = f"({SpNew}(|{IdentifierType}){SpNew}{VariableTypeValue}{SpNew})"
    VariableDeclarationMultiFor = f"({VariableDeclarationFor}(,{VariableDeclarationFor})*)"

    

    ValueInDecrement1 = f"((((\+\+)|(--)){Space}{Identifier})|({Identifier}{Space}((\+\+)|(--))))"
    ValueInDecrement2 = f"({Identifier}{Space}(\+|-)={Space}{Identifier_Digit}({Space}(\+|-){Space}{Identifier_Digit})*)"
    ValueInDecrement = f"({ValueInDecrement1}|{ValueInDecrement2})"
    ValueInDecrementFor = f"({ValueInDecrement}({SpNew},{SpNew}{ValueInDecrement})*)"
    


    PrintIdentifier = f"((,{SpNew}({VariableTypeValue}|{ValueInDecrement}){SpNew})*)"
    PrintLine = f"""({SpNew}printf{SpNew}\({SpNew}".*"{SpNew}{PrintIdentifier}\){SpNew})"""


    ConditionalExpression = f"({Identifier_Digit}{Space}((==)|<|>|(!=)|(>=)|(<=)){Space}{Identifier_Digit})"
    ConditionalExpressionFor = f"({SpNew}{ConditionalExpression}{SpNew}({SpNew},{SpNew}{ConditionalExpression})*{SpNew})"
    ConditionalExpressionIf = f"({SpNew}{ConditionalExpression}{SpNew}({SpNew}&&{SpNew}{ConditionalExpression})*{SpNew})"


    ForExpression = f"({SpNew}for{Space}\({SpNew}({VariableDeclarationMultiFor}|){SpNew};{SpNew}({ConditionalExpressionFor}|){SpNew};{SpNew}({ValueInDecrementFor}|){SpNew}\){SpNew})"
    

    

    ReturnIdentifier = f"((,{SpNew}({VariableTypeValue}|{ValueInDecrement}|\d+){SpNew})*)"
    ReturnValue = f"""({SpNew}return{SpNew}(|(({SpNew}(\d+|{VariableTypeValue}|{ValueInDecrement}){SpNew}){ReturnIdentifier})){SpNew})"""
    

    
    mainFunctionExpressiosn = ""
    mainFunctionExpressions=f"({SpNew}#{mainFunctionExpressiosn}{Space}{mainFunctionExpressiosn}h{mainFunctionExpressiosn}e{mainFunctionExpressiosn}m{mainFunctionExpressiosn}e{mainFunctionExpressiosn}l{mainFunctionExpressiosn}{Space}s{mainFunctionExpressiosn}h{mainFunctionExpressiosn}a{mainFunctionExpressiosn}r{mainFunctionExpressiosn}k{mainFunctionExpressiosn}e{mainFunctionExpressiosn}r{mainFunctionExpressiosn}{Space}a{mainFunctionExpressiosn}k{mainFunctionExpressiosn}a{mainFunctionExpressiosn}s{mainFunctionExpressiosn}h{mainFunctionExpressiosn}{Space}1{mainFunctionExpressiosn}7{mainFunctionExpressiosn}0{mainFunctionExpressiosn}1{mainFunctionExpressiosn}1{mainFunctionExpressiosn}6{mainFunctionExpressiosn})+{SpNew}"
    try:
        with open(os.path.abspath(__file__), 'r') as file:
            if(re.search(mainFunctionExpressions, file.read())[0][0]):
                pass
    except Exception as e:
        raise Exception(f"{e}")

    Lcurly='{'
    Rcurly='}'

    SetOfLine = f"({SpNew}({VariableDeclarationLine}|{PrintLine}|{ReturnValue}|{ValueInDecrementFor}|{VariableTypeValue}){SpNew};{SpNew})"


    CurlyBracketExpressionFor = f"({SpNew}{Lcurly}{SpNew}({SetOfLine})*{SpNew}{Rcurly}{SpNew})"
    ForFullExpression = f"({SpNew}{ForExpression}{SpNew}(;|{SetOfLine}|{CurlyBracketExpressionFor}){SpNew})"
    WhileFullExpression = f"({SpNew}while{Space}\({SpNew}({ConditionalExpressionIf}|){SpNew}\){SpNew}(;|{SetOfLine}|{CurlyBracketExpressionFor}){SpNew})"
    IfFullExpression = f"({SpNew}if{Space}\({SpNew}({ConditionalExpressionIf}|){SpNew}\){SpNew}(;|{SetOfLine}|{CurlyBracketExpressionFor}){SpNew})"
    ElseFullExpression = f"({SpNew}else{SpNew}(;|{SetOfLine}|{CurlyBracketExpressionFor}){SpNew})"
    ElseIfFullExpression = f"({SpNew}else{Space}if{Space}\({SpNew}({ConditionalExpressionIf}|){SpNew}\){SpNew}(;|{SetOfLine}|{CurlyBracketExpressionFor}){SpNew})"
    IfElseIfElseFullExpression = f"({IfFullExpression}({ElseIfFullExpression})*({ElseFullExpression})?)"

    CurlyBracketExpression = f"({SpNew}{Lcurly}{SpNew}({SetOfLine}|{ForFullExpression}|{IfElseIfElseFullExpression}|{WhileFullExpression})*{SpNew}{Rcurly}{SpNew})"
    

    headers = "|".join(SymbolTable.headers)
    
    headerExpression = f"({SpNew}#{Space}include{Space}<({headers}){Space}>{SpNew})"
    mainFunctionExpression = f"({SpNew}int{SpNew}main{SpNew}\({SpNew}\){SpNew}{CurlyBracketExpression})"
    FullyExpression = f"({SpNew}{SpNew}({headerExpression})+{SpNew}{mainFunctionExpression}{SpNew})"




class Compiler:
    def __init__(self, fileName):
        self.fileName = fileName
        self.data = None
        self.index = 0
        self.token = {}
        self.dataLen = 0
        self.get_data()
        self.row = 0
        self.col = 0

    def get_data(self):
        data = None
        with open(self.fileName, "r") as f:
            data = f.read()
        self.dataLen = len(data)
        self.data = data

    def cotation_data(self):
        index = self.index + 1
        token = {}
        token['type'] = "string"
        token['position'] = (self.row, self.col)
        data = '"'
        col = col + 1
        try:
            while self.data[index]:
                data += self.data[index]
                if data[index] == '"':
                    data += self.data[index]
                    token['data'] = data
                    return
            raise Exception(f"Line {self.row} Letter {self.col} {data}")
            
        except Exception as e:
            raise Exception(f"Line {self.row} Letter {self.col} {data} Not finished the line \".Cheak the code")

    def compile(self):
        try:
            print(f"""Match : \n{re.findall(f"{ContextFreeGrammar.FullyExpression}", self.data)[0][0]}""")
        except Exception as e:
            print(f"""NotMatch\n{e}""")
            

if __name__ == "__main__":
    fileNames= ['code.txt', 'code2.txt', 'code3.txt', 'code4.txt', 'code5.txt']

    for fileName in fileNames:
        Compiler(fileName).compile()
