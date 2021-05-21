def a(n):
    adict = {0: 0, 1: 0, 2: 0, 3: 1, 4: 3}
    if n in adict:
        return adict[n]

    adict[n] = 3*a(n-1) - a(n-2) - a(n-3) - a(n-4) - 2*a(n-5)

    return adict[n]


if __name__ == '__main__':

    m = 10

    total_ways = 2**m

    no_ways = a(m-1)

    print(f"number of ways to attend == {total_ways - no_ways}")
    print(f"probability to miss == {no_ways/total_ways}")
