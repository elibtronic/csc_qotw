
###
## Hailstorm function
#
#

def hailstorm(n, h):
    if n == 1:
       h.append(n)
       return
    elif n % 2 == 0:
        h.append(n)
        hailstorm(int(n/2),h)
    else:
        h.append(n)
        hailstorm(int(3*n+1),h)


h_long = []
h_temp = []
longest_seed = 0
longest_chain = 0

for n in range(3,4):
    hailstorm(n,h_temp)
    if len(h_temp) > longest_chain:
        h_long = []
        h_long = h_temp
        longest_seed = n
        longest_chain = len(h_temp)
    h_temp = []

print "Longest Chain Seed: ",longest_seed
print "sequence: ",h_long
