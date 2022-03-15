zoom, flash = int(input()), int(input())
if flash > zoom:
    print('YES')
elif zoom > flash:
    print('NO')
else:
    print("Don't know")

# modified
# zoom, flash = int(input()), int(input())
# print("Don't know" if zoom == flash else "YES" if flash < zoom else "NO")
