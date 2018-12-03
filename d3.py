#!/usr/bin/env python3

import re

if __name__ == "__main__":
    with open("d3.in") as inp:
        fabric = [[(0,0)]*1000 for i in range(1000)]
        claims = []
        for line in inp:
            m = re.search("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)", line)
            claim_id = int(m.group(1)); claims.append(claim_id)
            start_x = int(m.group(2)); start_y = int(m.group(3))
            width = int(m.group(4)); height = int(m.group(5))
            
            for i in range(start_x, start_x+width):
                for j in range(start_y, start_y+height):
                    n = fabric[i][j][1]
                    if n > 0:
                        if fabric[i][j][0] in claims:
                            claims.remove(fabric[i][j][0])
                        if claim_id in claims:
                            claims.remove(claim_id)

                    fabric[i][j] = (claim_id, n+1)
        print (claims)

#        shared_inches = 0
#        for i in range(1000):
#            for j in range(1000):
#                if fabric[i][j][1] > 1:
#                    shared_inches+=1
#        print (shared_inches)
