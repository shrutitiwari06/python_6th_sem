for i in range(int(input())):

    m,x,y=map(int,input().split())

    l=list(map(int,input().split()))

    k=x*y

    a=[i for i in range(100)]

    p=[]

    for i in l:

        if i<=k:

            p.extend(a[:i+k])

        else:

            p.extend(a[i-k-1:i+k])

    p=list(set(p))

    print(100-len(p))
