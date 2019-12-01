#!/usr/bin/env python3
# coding: utf-8


import os


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1(data):
    for line in data:
        print(line)


def part2(data):
    for line in data:
        print(line)


def main():
    with open(inputfile) as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
