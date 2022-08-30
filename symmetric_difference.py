if __name__ == '__main__':
    M = int(raw_input())
    list_1 = map(int, raw_input().split())
    N = int(raw_input())
    list_2 = map(int, raw_input().split())
    
    newlist1, newlist2 = list(map(int, list_1)), list(map(int, list_2))
    set_1, set_2 = set(newlist1), set(newlist2) 
    dif_1, dif_2 = set_1.difference(set_2), set_2.difference(set_1)
    difference = list(dif_1.union(dif_2))
    difference.sort()
    symmetric_difference = set()
    symmetric_difference.update(difference)
    for element in symmetric_difference:
        print(element)
    
