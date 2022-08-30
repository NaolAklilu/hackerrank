if __name__ == '__main__':
    M = int(raw_input())
    english = set(map(int, raw_input().split()))
    N = int(raw_input())
    french = set(map(int, raw_input().split()))
    
    print(len(english.union(french)))
