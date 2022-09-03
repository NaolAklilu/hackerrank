n = int(input())
elements = set(map(int, input().split()))

for _ in range(0, int(input())):
    command_entry = input().split()
    if command_entry[0] == 'pop':
        elements.pop()
    elif command_entry[0] == 'remove' and int(command_entry[1]) in elements:
        elements.remove(int(command_entry[1]))
    elif command_entry[0] == 'discard':
        elements.discard(int(command_entry[1]))
        
print(sum(elements))
