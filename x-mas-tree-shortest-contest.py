import sys
n=int(sys.argv[1])if len(sys.argv)>1 else 7
[print(x.center(n*2))for x in[((2*i+1)*'*')if i<n else'|'for i in range(n+2)]]
