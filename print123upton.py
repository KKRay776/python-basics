if __name__ == '__main__':
    n = int(input(''))
    num=0
    for i in range (1,n+1):
        num=num*10 +i
        
print(num)
#num = 0
# → 0*10 + (i)1 = 1
# → 1*10 + 2 = 12
# → 12*10 + 3 = 123
# → 123*10 + 4 = 1234
# → 1234*10 + 5 = 12345
#or something like thatf __name__ == '__main__':
#   if__name__ == '__main__': 
#     n = int(input())
    
#     print(*range(1,n+1),sep="")
        
# *printrange(1,n+1),sep="") is a more concise way to achieve the same result. It uses the unpacking operator (*) to unpack the range of numbers from 1 to n and prints them without any separator (sep="").