from itertools import combinations

if __name__ == "__main__":
    N = int(input())
    letters_lst = list(input().split())
    M = int(input())
    
    combination_list = list(combinations(letters_lst, M))
    count = 0
    
    for j in combination_list:
        if 'a' in j:
            count += 1
    print(format(count/len(combination_list)))
