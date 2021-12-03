import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Advent of Code 2021 Day 3')
    parser.add_argument('-f', '--filename', metavar='FILENAME', type=str, help='name of input file', default='inp03.txt')
    args = parser.parse_args()
    return args



def get_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
    return lines



def answer1(inp):
    counts = [0] * len(inp[0])
    for line in inp:
        for i in range(len(line)):
            if line[i] == '1':
                counts[i] += 1
    gamma = [str(int(i > (len(inp)) / 2)) for i in counts]
    eps = [str(int(i < (len(inp)) / 2)) for i in counts]
    gamma = int(''.join(gamma), 2)
    eps = int(''.join(eps), 2)
    return eps * gamma



def answer2(inp):
    i, curr = 0, inp
    while len(curr) > 1:
        ones, zeros = [], []
        numOnes, numZeros = 0, 0
        for line in curr:
            if line[i] == '1':
                numOnes += 1
                ones.append(line)
            else:
                numZeros += 1
                zeros.append(line)
        if numOnes >= numZeros:
            curr = ones
        else:
            curr = zeros
        i += 1
    oxy = int(curr[0], 2)
    i, curr = 0, inp
    while len(curr) > 1:
        ones, zeros = [], []
        numOnes, numZeros = 0, 0
        for line in curr:
            if line[i] == '1':
                numOnes += 1
                ones.append(line)
            else:
                numZeros += 1
                zeros.append(line)
        if numOnes < numZeros:
            curr = ones
        else:
            curr = zeros
        i += 1
    co2 = int(curr[0], 2)
    return oxy * co2



def main():
    args = parse_args()
    inp = get_input(args.filename)
    print("Answer 1:", answer1(inp))
    print("Answer 2:", answer2(inp))



if __name__ == '__main__':
    main()
