#!/usr/bin/env python3
# coding: utf-8


import os


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1():
    with open(inputfile) as file:
        for line in file:
            print(line)


def part2():
    with open(inputfile) as file:
        for line in file:
            print(line)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
