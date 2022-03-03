#This code is given b

#import math

for _ in range(int(input())):

      a,b=map(int,input().split())

      s=0

      for i in range(1,b+1):

            s=max(s,a%i) 

      print(s)
