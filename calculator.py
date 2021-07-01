import sys
sys.setrecursionlimit = 100000

def exp(a,b): return int(a) ** int(b)

def mul(a,b):    return int(a) * int(b)

def div(a,b):    return int(a) / int(b)

def add(a,b):    return int(a) + int(b)

def sub(a,b):    return int(a) - int(b)

operator = {"+":add,"-":sub,"*":mul,"/":div, "^":exp}

def check(xpr:str):    return xpr.count("(") == xpr.count(")")

def redundant(xpr:str):
    i = 0
    while i < len(xpr):
        if xpr[i] == "(" and xpr[i+2] == ")":
            xpr = xpr[:i] + xpr[i+1] + xpr[i+3:]
        i += 1
    return xpr

def calculate(xpr:str, i):
    buffer = ""
    while i < len(xpr):
        if xpr[i].isdigit() or xpr[i] in operator:
            buffer += xpr[i]
        elif xpr[i] == "(":
            temp, index = calculate(xpr, i+1)
            buffer += str(parse(temp))
            i = index + 1
        elif xpr[i] == ")":
            return buffer, i-1
        i += 1
    return buffer, i

def parse(xpr:str):
    if xpr.isdigit():
        return int(xpr)

    for optr in operator.keys():
        l,op,r = xpr.partition(optr)
        if op in operator:
            return operator[op](parse(l),parse(r))

if __name__=='__main__':
    print("Welcome to Simple Calculator!\nEnter your expression to be calculated, or type 'exit' to exit.")
    while True: 
        xpr = input('>>> ').replace(" ","")
        if xpr.lower() == 'exit':
            print("Exiting...")
            break
        else:
            if check(xpr):
                xpr = redundant(xpr)
                new_xpr, i = calculate(xpr, 0)
                print(parse(new_xpr))
            else:
                print("Invalid expression, mismatched parentheses.")