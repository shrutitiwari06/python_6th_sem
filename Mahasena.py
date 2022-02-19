N = int(input())
A = list(map(int, input().split()))[:N]
ecount = 0
ocount = 0
for i in A:
    if i % 2 == 0:
        ecount += 1
    else:
        ocount += 1
if ecount > ocount:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
