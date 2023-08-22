all = input().split()
pro = ['Alice', 'Bob', 'Cindy', 'Dani']
notin = []
for val in pro:
    if val not in all:
        notin.append(val)
print(str(notin).replace('[', '').replace(']','').replace("'",'').replace(',',''))