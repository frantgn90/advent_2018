#!/usr/bin/env python3

import bisect


if __name__ == "__main__":
    result = counter = 0
    partial_results = [result]
    with open("d1.in") as inp:
        while True:
            for line in inp:
                result += int(line)
                i = bisect.bisect_left(partial_results, result)
                if len(partial_results) > i and partial_results[i] == result:
                    print (result)
                    exit(0)
                else:
                    partial_results.insert(i, result)
            inp.seek(0)
            counter +=1
    exit (1)
