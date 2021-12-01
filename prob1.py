def getInput():
    with open("inp01.txt") as f:
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
    inp = getInput()
    a1, a2 = answer1(inp), answer2(inp)
    print("Answer 1:", a1)
    print("Answer 2:", a2)


if __name__ == '__main__':
    main()

