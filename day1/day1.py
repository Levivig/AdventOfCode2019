#!/usr/bin/env python3
# coding: utf-8


import os


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1():
    with open(inputfile) as file:
        total = 0
        for line in file:
            mass = int(line)
            total += int(mass / 3.0) - 2
        print("Part 1: {total}".format(total=total))


def getFuelFor(mass):
    if mass <= 0:
        return 0
    fuel = int(mass / 3.0) - 2
    if fuel <= 0:
        return 0
    return fuel + getFuelFor(fuel)


def part2():
    with open(inputfile) as file:
        total = 0
        for line in file:
            mass = int(line)
            total += getFuelFor(mass)
        print("Part 2: {total}".format(total=total))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
