# -*- coding: utf-8 -*-


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print 'usage: python RPN.py <expression>'
        exit(0)
    expression = sys.argv[1]
    print '[%s]' % expression
    stack = []
    def add(x, y):
        return x + y
    def sub(x, y):
        return x - y
    def mul(x, y):
        return x * y
    def div(x, y):
        return x / y
    operation = {'+':add, '-':sub, '*':mul, '/':div}
    for i, s in enumerate(expression):
        if i > 0: print stack
        if s not in operation.keys():
            stack.append(int(s))
        else:
            y = stack.pop()
            x = stack.pop()
            print '%d %s %d' % (x, s, y)
            stack.append(operation[s](x, y))
    print stack
