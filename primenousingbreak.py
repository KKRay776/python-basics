lower = int(input('enter the lower'))
upper = int(input('enter the upper'))

for i in range(lower, upper+1):      # Loop through all numbers in the range
    for j in range(2, i):            # Check divisibility from 2 up to i-1
        if i % j == 0:               # If divisible, it's not prime
            break                    # Exit inner loop early
    else:                            # This else belongs to the 'for j' loop
        print(i)                     # If no divisor found, print i (prime)