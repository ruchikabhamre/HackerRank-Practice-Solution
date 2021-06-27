A = set(raw_input().split());


print all(map(lambda x: (A > x), [set(raw_input().split()) for i in range(int(raw_input()))])) 