for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            for d in range(1, 10):
                num = str(a) + str(b) + str(c) + str(d)
                num_reverse = str(d) + str(c) + str(b) + str(a)
                #print(num, num_reverse)
                if int(num) == 4 * int(num_reverse):
                    print(num, num_reverse)