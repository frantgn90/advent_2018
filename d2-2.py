#!/usr/bin/env python3

def ndifs(a,b):
    difs = 0
    for i in range(0,len(a)):
        if a[i] != b[i]:
            difs+=1
    return difs

def diff(a,b):
    d = ""
    for i in range(0,len(a)):
        if a[i] == b[i]:
            d+=a[i]
    return d

if __name__ == "__main__":
    f1 = open("d2.in")
    f2 = open("d2.in")

    for l in f1:
        for l2 in f2:
            if ndifs(l,l2) == 1:
                print (diff(l,l2))
                exit(0)
        f2.seek(0)
    close(f1)
    close(f2)
