# https://www.hackerrank.com/challenges/greedy-florist/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
# !/bin/python3

# Complete the getMinimumCost function below.
def getMinimumCost1(k, c):
    c.sort(reverse=True)
    total = 0
    rounds = 1
    for f,p in enumerate(c):
        total += rounds * p
        if not (f+1)%k:
            rounds += 1
    return total

def getMinimumCost2(k, c):
    counter = 0
    div = k
    sum = 0
    i = len(c)-1
    while i >= 0:
        if k>0:
            sum +=c[i]
            counter +=1
        else:
            sum += ( int (counter/div) + 1 ) * c[i]
        i -=1
        k -=1
    return sum

def getMinimumCost(k, c):
    c.sort()
    sum = 0
    for i in range(len(c)-1,-1,-1):
       sum +=  ( int ( ( len(c)-1 -i ) / k ) + 1 ) * c[i]
    return sum


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    print(minimumCost)

    # fptr.write(str(minimumCost) + '\n')
    # fptr.close()
