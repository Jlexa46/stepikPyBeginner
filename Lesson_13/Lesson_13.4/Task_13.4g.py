def quick_merge():
    list = []
    for _ in range(int(input())):
        list += [int(i) for i in input().split()]
    list.sort()
    print(*list)

quick_merge()
