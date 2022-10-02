"""
INPUT = “programmerffdaprogrammer”
Output = 4 

INPUT = “proofasdrsgrammeeqsrggspsacrdvograqwmmeer”
Output = 3

INPUT = "asdfeqrvfpgormarerproofasdrsgrammeeqsrg" 
Output = -1 
"""

# --> P r o g r a m m e [r]          <--- [P] r o g r a m m e r       
def programmer(input):
    _string = "programmer"
    word1 = 0
    count = 0
    word2 = 0
    tmp = 0

    for i in range(len(input)-1):
        if _string[count] == input[i]:
            count = count + 1
            if len(_string) == count:
                word1 = i
                k2 = i
                break
    count = 0
    for i in range(word1, len(input)):
        if _string[0] == input[i]: # Start of P 
            tmp = i
        
        if _string[count] == input[i]:
            count += + 1
            if count == len(_string):
                word2 = tmp
    if count != len(_string): # If Programmer not exist in string
        print("Not exist")
        return -1
    
    print("First ", word1, "Second ", word2)
    print(word2 - word1)
            
def main():
    programmer("programmerffdaprogrammer")

main()
