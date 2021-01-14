from lr1_analyzer import LR1


def main():
    chain = input('Input chain: ')
    lr1 = LR1(chain, 'BBTTMM', ['B+T', 'T', 'T*M', 'M', '(B)', 'И'])
    print(lr1.analyze())


if __name__ == '__main__':
    main()
