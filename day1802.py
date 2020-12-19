
def evaluate(phrase):

    left = 0
    operator = ''
    right = 0
    result = 0

    todo = []
    space1 = phrase.find(' ')
    if space1 == -1:
        return int(phrase)

    i = 0
    while i < len(phrase):
        if phrase[i] == '(':
            parens = 1
            newphrase = ""
            for c in phrase[i+1:]:
                if c == '(':
                    parens += 1
                elif c == ')':
                    parens -= 1
                    if parens == 0:
                        break
                newphrase += c
            todo.append(evaluate(newphrase))
            i += len(newphrase) + 1
        elif phrase[i] in ['+','-','*','/']:
            todo.append(phrase[i])
        elif phrase[i]  == ' ':
            i += 1
            continue
        else: # it must be an integer
            space1 = phrase[i:].find(' ')
            if space1 == -1:
                todo.append(int(phrase[i:]))
            else:
                todo.append(int(phrase[i:i+space1]))
        i += 1

    while '+' in todo:
        i = todo.index('+')
        todo[i-1] = todo[i-1] + todo[i+1]
        todo.pop(i)
        todo.pop(i)

    result += todo[0]
    for i in range(1,len(todo)):
        if todo[i] == '+':
            result += todo[i+1]
        elif todo[i] == '*':
            result *= todo[i+1]
        if todo[i] == '/':
            result /= todo[i+1]
        if todo[i] == '-':
            result -= todo[i+1]

    return result


with open("day18.txt", "r") as f:
    sum = 0
    for line in f:
        e = evaluate(line.strip())
        print(e)
        sum += e

print(sum)