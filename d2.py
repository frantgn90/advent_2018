#!/usr/bin/env python3

if __name__ == "__main__":
    with open("d2.in") as inp:
        count_exact_two = 0
        count_exact_three = 0
        for line in inp:
            exact_two = False
            exact_three = False
            box_id = sorted(line)

            cnt = 1
            letter = box_id[0]
            for i in range(1,len(box_id)):
                if box_id[i] == letter:
                    cnt+=1
                else:
                    if cnt == 2:
                        exact_two = True
                    elif cnt == 3:
                        exact_three = True
                    if exact_two and exact_three:
                        break

                    letter = box_id[i]
                    cnt=1
            if cnt == 2:
                exact_two = True
            if cnt == 3:
                exact_three = True

            if exact_two:
                count_exact_two+=1
            if exact_three:
                count_exact_three+=1
    print (count_exact_two*count_exact_three)




