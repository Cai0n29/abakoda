code = input()

if code[-9:] == '...---...' or code[:9] == '...---...':
    print('SOS')
else:
    print('Hay SOS!')
