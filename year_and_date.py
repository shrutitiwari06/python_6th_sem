date=input("enter date in mm:dd:yyyy ")

m=int(date[0:2])
d=int(date[3:5])
y=int(date[6:10])

if(m==1):
  print("jan",d,y)
elif(m==2):
  print("feb",d,y)
elif(m==3):
  print("march",d,y)
elif(m==4):
  print("April",d,y)
elif(m==5):
  print("may",d,y)
elif(m==6):
  print("june",d,y)
elif(m==7):
  print("july",d,y)
elif(m==8):
  print("August",d,y)
elif(m==9):
  print("sept",d,y)
elif(m==10):
  print("Oct",d,y)
elif(m==11):
  print("Nov",d,y)
else:
  print("Dec",d,y)
