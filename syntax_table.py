class SyntaxTable:
    """
    Syntax table consists of 2 parts
    s - transfer
    r - convolution
    er - error (empty position)
    """
    action = [
        [['s', 5], 'er', 'er', ['s', 4], 'er', 'er'],
        ['er', ['s', 6], 'er', 'er', 'er', 'ex'],
        ['er', ['r', 2], ['s', 7], 'er', ['r', 2], ['r', 2]],
        ['er', ['r', 4], ['r', 4], 'er', ['r', 4], ['r', 4]],
        [['s', 5], 'er', 'er', ['s', 4], 'er', 'er'],
        ['er', ['r', 6], ['r', 6], 'er', ['r', 6], ['r', 6]],
        [['s', 5], 'er', 'er', ['s', 4], 'er', 'er'],
        [['s', 5], 'er', 'er', ['s', 4], 'er', 'er'],
        ['er', ['s', 6], 'er', 'er', ['s', 11], 'er'],
        ['er', ['r', 1], ['s', 7], 'er', ['r', 1], ['r', 1]],
        ['er', ['r', 3], ['r', 3], 'er', ['r', 3], ['r', 3]],
        ['er', ['r', 5], ['r', 5], 'er', ['r', 5], ['r', 5]]
    ]
    goto = [
        [1, 2, 3],
        ['er', 'er', 'er'],
        ['er', 'er', 'er'],
        ['er', 'er', 'er'],
        [8, 2, 3],
        ['er', 'er', 'er'],
        ['er', 9, 3],
        ['er', 'er', 10],
        ['er', 'er', 'er'],
        ['er', 'er', 'er'],
        ['er', 'er', 'er'],
        ['er', 'er', 'er']
    ]
