#!/usr/bin/env python3

import re, sys

def nearest_city(i,j,cities):
    dists = list(map(
        lambda x: (x[0], abs(i-x[1][0])+abs(j-x[1][1])), 
        enumerate(cities)))
    dists.sort(key=lambda x: x[1])

    if dists[0][1] == dists[1][1]: return -1
    else: return dists[0][0]

if __name__ == "__main__":
    with open("d6.in") as inp:
        cities = []
        min_x = min_y = sys.maxsize
        max_x = max_y = 0
        for line in inp:
            m = re.search("^([0-9]+), ([0-9]+)$", line)
            x = int(m.group(1)); y = int(m.group(2))
            if   x < min_x: min_x = x
            elif x > max_x: max_x = x
            if   y < min_y: min_y = y
            elif y > max_y: max_y = y
            cities.append((x,y))

    width  = max_x-min_x+1; height = max_y-min_y+1

    cities_points = [0]*(len(cities)+1)
    cities_in_bounds = set()
    cities = list(map(lambda x: (x[0]-min_x, x[1]-min_y), cities))
    for i in range(width):
        for j in range(height):
            city = nearest_city(i,j, cities)
            if (i == 0 or i == width-1 or j == 0 or j == height-1) \
                    and city != -1:
                        cities_in_bounds.add(city)
            cities_points[city] += 1

    max_points = 0
    for i,p in enumerate(cities_points):
        if not i in cities_in_bounds:
            if p > max_points: max_points = p
    print (max_points)
