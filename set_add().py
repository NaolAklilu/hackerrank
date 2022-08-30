if __name__ == '__main__':
    N = int(raw_input())
    country_stamp = set()
    for _ in range(0, N):
        country = raw_input()
        country_stamp.add(country)
        
    print(len(country_stamp))
