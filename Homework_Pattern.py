print("Half Pyramid pattern of stars")
n= int(input("Enter the number of rows:"))
k=" "
for i in range(1,n+1,1):
    k=" "
    for j in range (0,n+1,1):
      if j<n-i:
          k=k+" "
      elif j>=n-i and j<n:
         k=k+"*"
      else:
         print(k)
         
         