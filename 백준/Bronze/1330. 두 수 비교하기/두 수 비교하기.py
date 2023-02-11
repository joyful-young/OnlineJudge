input_data = input().split(' ')
A = int(input_data[0])
B = int(input_data[1])

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')