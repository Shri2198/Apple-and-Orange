def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apples = 0
    count_oranges = 0
    c = []
    d = []
    for i in range(0,len(apples)):
        c.append(apples[i] + a)


    for j in range(0,len(oranges)):
        d.append(oranges[j] + b)

    for x in c:
        if x in range(s,t+1):
            count_apples += 1
    for y in d:
        if y in range(s,t+1):
            count_oranges += 1

    print (count_apples)
    print (count_oranges)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
