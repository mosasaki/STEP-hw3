def readNumber(line, index):
    """Invert string to float and create dictionary for the token"""

    number = 0

    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1

    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta /= 10
            index += 1

    token = {'type': 'NUMBER', 'number': number}

    return token, index


def readPlus(line, index):
    """Create dictionary for the token"""

    token = {'type': 'PLUS'}
    return token, index + 1


def readMinus(line, index):
    """Create dictionary for the token"""

    token = {'type': 'MINUS'}
    return token, index + 1

def readMulitply(line, index):
    """Create dictionary for the token"""

    token = {'type': 'MULTIPLY'}
    return token, index + 1

def readDivide(line, index):
    """Create dictionary for the token"""

    token = {'type': 'DIVIDE'}
    return token, index + 1

def tokenize(line):
    """Determine if a string is number/+/-/×/÷ and make list of tokens"""

    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMulitply(line, index)
        elif line[index] == '/':
            (token, index) = readDivide(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens


def evaluate_plus_minus(tokens):
    """Solve addition & subtraction and return the answer """
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                if tokens[index - 1]['type'] in ('DIVIDE', 'MULTIPLY'):
                    index += 1
                else:
                    print('Invalid syntax')
                    exit(1)

        index += 1
    return answer

def evaluate_multiply_divide(tokens):
    """Solve multiplication & division and update the list of tokens"""
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    tokens.insert(0, {'type': 'PLUS'})  # Insert a dummy '+' token
    index = 2
    end = len(tokens)

    while index < end:
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'MULTIPLY':
                tokens[index - 2]['number'] *= tokens[index]['number']
                tokens.pop(index)
                tokens.pop(index - 1)
                index -= 2
                end -= 2
            elif tokens[index - 1]['type'] == 'DIVIDE':
                tokens[index - 2]['number'] /= tokens[index]['number']
                tokens.pop(index)
                tokens.pop(index - 1)
                index -= 2
                end -= 2
            else:
                if tokens[index - 1]['type'] in('PLUS', 'MINUS'):
                    index += 1
                else:
                    print('Invalid syntax')
                    exit(1)
        index += 1
    return tokens


def evaluate(tokens):
    """Evaluate the list of tokens and return an answer"""
    answer = evaluate_plus_minus(evaluate_multiply_divide(tokens))
    return answer

def test(line):
    """Testing to see if this calculator program works"""
    tokens = tokenize(line)
    actualAnswer = evaluate(tokens)
    expectedAnswer = eval(line)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expectedAnswer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
    """Specific equations for test"""
    print("==== Test started! ====")
    test("1")
    test("1+2")
    test("1.0+2")
    test("1.0+2.1-3")
    test("3*3")
    test("3*3.0")
    test("2+3*3.0")
    test("2-3*3.0+2")
    test("3/3")
    test("2+3/3")
    test("2+4*6/2.0-3.0")
    test("2+4*6/2.0-6.0/3*2")
    print("==== Test finished! ====\n")


runTest()


while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)