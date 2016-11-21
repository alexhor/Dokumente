class Expression:
    def evaluate(self):
        return 0;


class AdditionExpression(Expression):
    def __init__(self, summand1, summand2):
        self.summand1 = summand1
        self.summand2 = summand2

    def evaluate(self):
        return self.summand1.evaluate() + self.summand2.evaluate()


class SubtractionExpression(Expression):
    def __init__(self, minuend, subtrahend):
        self.minuend = minuend
        self.subtrahend = subtrahend

    def evaluate(self):
        return self.minuend.evaluate() - self.subtrahend.evaluate()


class MultiplicationExpression(Expression):
    def __init__(self, factor1, factor2):
        self.factor1 = factor1
        self.factor2 = factor2

    def evaluate(self):
        return self.factor1.evaluate() * self.factor2.evaluate()


class DivisionExpression(Expression):
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    def evaluate(self):
        divisor = self.divisor.evaluate()
        if divisor == 0:
            raise ZeroDivisionError
        return self.dividend.evaluate() / divisor;


class PowerExpression(Expression):
    def __init__(self, basis, exponent):
        self.basis = basis
        self.exponent = exponent

    def evaluate(self):
        return self.basis.evaluate() ** self.exponent.evaluate()


class FixedValueExpression(Expression):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


def parse(expression):
    return parseRec(expression, [])    


import re
linePattern = re.compile("(?:\\(\\s*([0-9.#]*)\\s*(\\+|-)\\s*([0-9.#]+)\\s*\\))|(?:([0-9.#]+)\\s*(\\+|-)\\s*([0-9.#]+))")
pointPattern = re.compile("(?:\\(\\s*([0-9.#]+)\\s*(\\*|\\/)\\s*([0-9.#]+)\\s*\\))|(?:([0-9.#]+)\\s*(\\*|\\/)\\s*([0-9.#]+))")
powerPattern = re.compile("(?:\\(\\s*([0-9.#]+)\\s*\\^\\s*([0-9.#]+)\\s*\\))|(?:([0-9.#]+)\\s*\\^\\s*([0-9.#]+))")
fixedValuePattern = re.compile("\\(?\\s*([\\+-]?\\s*[0-9.#]+)\\s*\\)?")


def parseRec(expression, embedded):
    ret = False
    
    matcher = powerPattern.search(expression)
    while matcher != None:
        ret = True
        if matcher.group(0).startswith("("):
            exp1 = embedded[int(matcher.group(1)[1:])] if matcher.group(1).startswith("#") else FixedValueExpression(float(matcher.group(1)))
            exp2 = embedded[int(matcher.group(2)[1:])] if matcher.group(2).startswith("#") else FixedValueExpression(float(matcher.group(2)))
        else:
            exp1 = embedded[int(matcher.group(3)[1:])] if matcher.group(3).startswith("#") else FixedValueExpression(float(matcher.group(3)))
            exp2 = embedded[int(matcher.group(4)[1:])] if matcher.group(4).startswith("#") else FixedValueExpression(float(matcher.group(4)))
        embedded.append(PowerExpression(exp1, exp2))
        expression = re.sub(powerPattern, "#" + str(len(embedded) - 1), expression)
        matcher = powerPattern.search(expression)
    
    matcher = pointPattern.search(expression)
    while matcher != None:
        ret = True
        if matcher.group(0).startswith("("):
            exp1 = embedded[int(matcher.group(1)[1:])] if matcher.group(1).startswith("#") else FixedValueExpression(float(matcher.group(1)))
            exp2 = embedded[int(matcher.group(3)[1:])] if matcher.group(3).startswith("#") else FixedValueExpression(float(matcher.group(3)))
            embedded.append(MultiplicationExpression(exp1, exp2) if matcher.group(2) == "*" else DivisionExpression(exp1, exp2))
        else:
            exp1 = embedded[int(matcher.group(4)[1:])] if matcher.group(4).startswith("#") else FixedValueExpression(float(matcher.group(4)))
            exp2 = embedded[int(matcher.group(6)[1:])] if matcher.group(6).startswith("#") else FixedValueExpression(float(matcher.group(6)))
            embedded.append(MultiplicationExpression(exp1, exp2) if matcher.group(5) == "*" else DivisionExpression(exp1, exp2))
        expression = re.sub(pointPattern, "#" + str(len(embedded) - 1), expression)
        matcher = pointPattern.search(expression)
    
    matcher = linePattern.search(expression)
    while matcher != None:
        ret = True
        if matcher.group(0).startswith("("):
            exp1 = FixedValueExpression(0.0) if not matcher.group(1) else embedded[int(matcher.group(1)[1:])] if matcher.group(1).startswith("#") else FixedValueExpression(float(matcher.group(1)))
            exp2 = embedded[int(matcher.group(3)[1:])] if matcher.group(3).startswith("#") else FixedValueExpression(float(matcher.group(3)))
            embedded.append(AdditionExpression(exp1, exp2) if matcher.group(2) == "+" else SubtractionExpression(exp1, exp2))
        else:
            exp1 = embedded[int(matcher.group(4)[1:])] if matcher.group(4).startswith("#") else FixedValueExpression(float(matcher.group(4)))
            exp2 = embedded[int(matcher.group(6)[1:])] if matcher.group(6).startswith("#") else FixedValueExpression(float(matcher.group(6)))
            embedded.append(AdditionExpression(exp1, exp2) if matcher.group(5) == "+" else SubtractionExpression(exp1, exp2))
        expression = re.sub(linePattern, "#" + str(len(embedded) - 1), expression)
        matcher = linePattern.search(expression)
    
    if ret:
        return parseRec(expression, embedded)

    matcher = fixedValuePattern.search(expression)
    if matcher != None:
        return embedded[int(matcher.group(1)[1:])] if matcher.group(1).startswith("#") else FixedValueExpression(float(matcher.group(1)))
    else:
        raise ArithmeticError


def evaluate(expression):
    return parse(expression).evaluate()


while True:
    expression = input("Eingabe: ")
    if expression == "exit":
        break
    else:
        print("Ergebnis: " + str(evaluate(expression)) + "\n")


















            
