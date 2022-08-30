def swap_case(s):
    new_string = s.swapcase()
    return new_string

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
