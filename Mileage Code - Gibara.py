n=int(input("Enter Electric Range:"))
if n == 0:
  print("Range has not been tested")
elif n<= 100:
        print("Short Range")
elif n > 100 and n <= 300 :
        print("Average Range")
else:
        print("Long Range")        
    