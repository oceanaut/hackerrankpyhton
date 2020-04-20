# https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms

# !/bin/python3
# Complete the luckBalance function below.
def luckBalance(k, contests):
    unimportant_sum = 0
    ktemp = 0
    l_important = []
    for i in contests:
        if i[1] == 0:
            unimportant_sum += i[0]
        elif i[1] == 1:
            l_important.append(i[0])
    l_important.sort(reverse=True)  # descending order
    for i in l_important:
        if ktemp < k:
            unimportant_sum += i
            ktemp += 1
        else:
            unimportant_sum -= i
    return unimportant_sum


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))
    result = luckBalance(k, contests)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()
