def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        start = i
        end = i + len(sub_string)
        if sub_string == string[start:end]:
            count += 1            
    return count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
