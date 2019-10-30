# opens file
f = 'word.txt'
file=open(f)

def histogram():
    di = dict()
    for lin in file:
        lin = lin.rstrip()
        # print(lin)
        wds = lin.split()
    # print(wds)
        for w in wds:

            if w in di:
                di[w] = di[w] + 1
            else:
                di[w]=1
            print(w, di[w])

    print(di)

histogram()
file.close()