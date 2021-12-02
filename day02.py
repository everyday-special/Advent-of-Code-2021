import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Advent of Code 2021 Day 2')
    parser.add_argument('-f', '--filename', metavar='FILENAME', type=str, help='name of input file', default='inp02.txt')
    args = parser.parse_args()
    return args



def get_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.split(' ') for line in lines]
    return lines



def answer1(inp):
    x, y = 0, 0
    for line in inp:                
        if line[0] == 'up':             
            y -= int(line[1].rstrip())                 
        elif line[0] == 'down':         
            y += int(line[1].rstrip())
        else:                         
            x += int(line[1].rstrip())
    return x * y



def answer2(inp):
    aim, x, y = 0, 0, 0
    for line in inp:
        if line[0] == 'up':
            aim -= int(line[1].rstrip())
        elif line[0] == 'down':
            aim += int(line[1].rstrip())
        else:
            x += int(line[1].rstrip())
            y += aim * int(line[1].rstrip())
    return x * y



def main():
    args = parse_args()
    inp = get_input(args.filename)
    print("Answer 1:", answer1(inp))
    print("Answer 2:", answer2(inp))



if __name__ == '__main__':
    main()
