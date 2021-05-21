def get_nth_tetranacci(n):
    adict = {0: 0, 1: 0, 2: 0, 3: 1, 4: 3}
    if n in adict:
        return adict[n]

    adict[n] = 3*get_nth_tetranacci(n-1) - get_nth_tetranacci(n-2) - get_nth_tetranacci(n-3) - get_nth_tetranacci(n-4) - 2*get_nth_tetranacci(n-5)

    return adict[n]


if __name__ == '__main__':

    N = int(input('Enter number of days:  '))

    total_ways = 2**N

    no_ways = get_nth_tetranacci(N-1)

    print(f"\nnumber of ways to attend == {total_ways - no_ways}")
    print(f"probability to miss == {no_ways/total_ways}")
