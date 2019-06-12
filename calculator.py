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


def read_open_paren(line, index):
    """Create dictionary for the token"""

    token = {'type': 'OPEN_PAREN'}
    return token, index + 1


def read_close_paren(line, index):
    """Create dictionary for the token"""

    token = {'type': 'CLOSE_PAREN'}
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
        elif line[index] == '(':
            (token, index) = read_open_paren(line, index)
        elif line[index] == ')':
            (token, index) = read_close_paren(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)

    return tokens


def evaluate_plus_minus(tokens):
    """Solve addition & subtraction and return the answer """

    answer = 0
    tokens.insert(0, {'type': 'PLUS'})  # Insert a dummy '+' token
    index = 1

    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1

    return answer


def evaluate_multiply_divide(tokens):
    """Solve multiplication & division and update the list of tokens"""

    tokens.insert(0, {'type': 'PLUS'})  # Insert a dummy '+' token
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
            elif tokens[index - 1]['type'] in('PLUS', 'MINUS'):
                index += 1
            else:
                print('Invalid syntax')
                exit(1)
        index += 1

    return tokens


def evaluate_parentheses(tokens):
    """Solve multiplication & division and update the list of tokens"""

    tokens.insert(0, {'type': 'PLUS'})  # Insert a dummy '+' token
    index = 1
    end = len(tokens)

    while index < end:
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'OPEN_PAREN':
                index_paren = index
                tmp_tokens = []
                while tokens[index_paren]['type'] != 'CLOSE_PAREN':
                    tmp_tokens.append(tokens[index_paren])
                    index_paren += 1
                tmp_ans = evaluate_plus_minus(evaluate_multiply_divide(tmp_tokens))
                tokens[index - 1]['number'] = tmp_ans
                tokens[index - 1]['type'] = 'NUMBER'
                while tokens[index]['type'] != 'CLOSE_PAREN':
                    tokens.pop(index)
                    end -= 1
                tokens.pop(index)
                end -= 1
            elif tokens[index - 1]['type'] in('PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'NUMBER'):
                index += 1
            else:
                print('Invalid syntax')
                exit(1)
        index += 1
        
    return tokens


def evaluate(tokens):
    """Evaluate the list of tokens and return an answer"""

    answer = evaluate_plus_minus(evaluate_multiply_divide(evaluate_parentheses(tokens)))
    return answer


while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)
