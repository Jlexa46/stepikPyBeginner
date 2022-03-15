city1, city2, city3 = input(), input(), input()
print(min(city1, city2, city3, key=len), max(city1, city2, city3, key=len), sep='\n')
