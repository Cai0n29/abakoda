a, b = input().split()
a = int(a)
b = int(b)
ar = input().split()
ar = [int(x) for x in ar]
br = input().split()
br = [int(i) for i in br]

print(max(sum(ar), sum(br)))