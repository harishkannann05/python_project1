def fib(n):
  n1=0
  n2=1
  print(n1,n2,sep="\n")
  while n-2>0:
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)
    n=n-1

n=int(input("Enter no of terms: "))
fib(n)