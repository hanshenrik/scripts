import sys
n=len(sys.argv)>1 and int(sys.argv[1])or 7
[print(x.center(n*2))for x in[('|',((2*i+1)*'*'))[i<n]for i in range(n+2)]]
