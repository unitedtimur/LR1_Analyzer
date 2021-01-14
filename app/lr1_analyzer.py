from app.non_terminals import NonTerminals
from app.syntax_table import SyntaxTable
from app.terminals import Terminals


class LR1:
    def __init__(self, chain: str, lr: list, rr: list):
        self.rules = []
        self.lr = lr
        self.rr = rr
        self.T = Terminals.T
        self.N = NonTerminals.N
        self.action = SyntaxTable.action
        self.goto = SyntaxTable.goto
        self.chain = list(chain + '$')

    def _makeRules(self):
        for i, j in zip(self.lr, self.rr):
            self.rules.append([i, j])

    def analyze(self):
        stack = [0]
        convolution = []
        reverse_polish_notation = []

        while True:
            symbol = self.chain[0]

            if symbol in ['a', 'b', 'c']:
                action = self.action[stack[len(stack) - 1]][self.T.index('И')]
            else:
                action = self.action[stack[len(stack) - 1]][self.T.index(symbol)]

            # Transition
            if action[0] == 's':
                stack.append(symbol)
                stack.append(action[1])
                self.chain.remove(symbol)
            # Convolution
            elif action[0] == 'r':
                convolution.append(action[1])
                l = 2 * len(self.rr[action[1] - 1])
                j = 0

                while j < l:
                    pop = stack.pop()
                    if (pop in self.T or pop in ['a', 'b', 'c']) and pop not in ['(', ')']:
                        reverse_polish_notation.append(pop)
                    j += 1

                a = self.lr[action[1] - 1]
                sm = stack[len(stack) - 1]
                stack.append(a)
                stack.append(self.goto[sm][self.N.index(a)])
            # It's okay
            elif action == 'ex':
                return f'Yeah! Check it out ;)\n' \
                       f'RPN: {reverse_polish_notation}\n' \
                       f'Сonvolution (Analysis): {convolution}'
            # It's bad
            elif action == 'er':
                return f'Oh know, smth wrong! ;(\n' \
                       f'RPN: {reverse_polish_notation}\n' \
                       f'Сonvolution (Analysis): {convolution}'

