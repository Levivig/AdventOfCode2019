#!/usr/bin/env python3
# coding: utf-8


import os


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def computer(data, noun=None, verb=None):
    idx = 0
    if noun != None:
        data[1] = noun
    if verb != None:
        data[2] = verb
    while len(data) > idx:
        if data[idx] == 99:
            break
        elif data[idx] == 1:
            left = data[data[idx+1]]
            right = data[data[idx+2]]
            data[data[idx+3]] = left + right
        elif data[idx] == 2:
            left = data[data[idx+1]]
            right = data[data[idx+2]]
            data[data[idx+3]] = left * right
        idx += 4

    # print(data[0])
    return data[0]


def part1():
    with open(inputfile) as file:
        for line in file:
            data = list(map(int, line.split(",")))
    print("Part1: {}".format(computer(data, 12, 2)))


def getData():
    with open(inputfile) as file:
        for line in file:
            return list(map(int, line.split(",")))

def part2():
    for idx in range(0,100):
        for jdx in range(0,100):
            data = getData()
            if computer(data, idx, jdx) == 19690720:
                print("Part2: {}".format(100 * 48 + 47))
                break




def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
