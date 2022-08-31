import math
if __name__ == '__main__':
    AB = int(input())
    BC = int(input())
    
    angle = round(math.degrees(math.atan(AB/BC)))
    
    print(str(angle) + chr(176))
