#!/usr/bin/env python3

def part1(polymer_chain):
    i = 1
    while i < len(polymer_chain):
        diff = ord(polymer_chain[i-1]) - ord(polymer_chain[i])
        if abs(diff) == 32:
            del polymer_chain[i]
            del polymer_chain[i-1]
            i=max(1, i-1)
        else:
            i+=1

    return len(polymer_chain)

def part2(polymer_chain):
    import string
    result = []
    for letter in string.ascii_lowercase:
        tmp_polymer_chain = list(
                filter(lambda x: x.lower() != letter, polymer_chain))
        result.append(part1(tmp_polymer_chain))
    result.sort()

    return result[0]


if __name__ == "__main__":
    with open("d5.in") as inp:
        polymer_chain = list(inp.readline()[:-1])

        #print (part1(polymer_chain))
        print (part2(polymer_chain))
