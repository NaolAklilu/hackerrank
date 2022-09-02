from collections import OrderedDict

N = int(input())
ordered_dictionary = OrderedDict()
item_list = []
for _ in range(0, N):
    entry = input().split()
    if len(entry) == 2:
        ordered_dictionary[entry[0]] = int(entry[-1])
        item_list.append(entry[0])
    else: 
        for i in range(1, len(entry)-1):
            entry[0] = entry[0] + " " + entry[i]
        ordered_dictionary[entry[0]] = int(entry[-1])
        item_list.append(entry[0])
 
ordered_dict = []
for item in ordered_dictionary.items():
    ordered_dict.append(list(item)) 

for item_price_pair in ordered_dict:
    numbers = item_list.count(item_price_pair[0])
    item_price_pair[1] *= numbers
    print(item_price_pair[0], item_price_pair[1])
    
