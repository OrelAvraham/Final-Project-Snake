with open('game_history/Orik.snake', 'r') as f:
    lines = f.read().split('\n')
    snake = eval(lines[0])
    lengths = eval(lines[1])
    foods = eval(lines[2])

    print(f'Snake[{len(snake)}]:{snake}')
    print(f'LENGTHS[{len(lengths)}]:{lengths}')
    print(f'Snake[{len(foods)}]:{foods}')

if __name__ == '__main__':
    pass