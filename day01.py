import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Advent of Code 2021 Day 1')
    parser.add_argument('-f', '--filename', metavar='FILENAME', type=str, help='name of input file', default='inp01.txt')
    args = parser.parse_args()
    return args



def getInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [int(line.rstrip()) for line in lines]
        return lines



def answer1(inp):
    count = 0
    for i in range(1, len(inp)):
        if inp[i] > inp[i-1]:
            count += 1
    return count



def answer2(inp):
    count = 0
    for i in range(3, len(inp)):
        prev = sum(inp[i-3:i])
        curr = sum(inp[i-2:i+1])
        if curr > prev:
            count += 1
    return count



def main():
    args = parse_args()
    inp = getInput(args.filename)
    a1, a2 = answer1(inp), answer2(inp)
    print("Answer 1:", a1)
    print("Answer 2:", a2)



if __name__ == '__main__':
    main()

