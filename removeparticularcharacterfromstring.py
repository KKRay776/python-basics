s=input('enter the string:')
term=input('enter the character to remove from the string:')
result=""#empty string is created to store final output
for i in s:#checks i in s

    if i!=term:#if i is not equall to term its sored in result if equall its get skipped
        result=result+i
print(result)