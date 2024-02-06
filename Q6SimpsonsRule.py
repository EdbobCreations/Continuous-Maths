#x^(3/2),a=0,b=2

def simpsonsRule(n):
    #Add y0
    total=funcCalculator(0)
    i=1
    while(i<n):
        if(i % 2 == 1):
            #If i is odd, add 4y(2i/n)
            total += 4 * funcCalculator(2/n * i)

        else:
            #If i is even, add 4y(2i/n)
            total += 2 * funcCalculator(2/n * i)

        i+=1
    #Add yn
    total += funcCalculator(2)
    h = 2/n
    total *= (h/3)
    return total
    



def funcCalculator(x):
    #Calculate x^(3/2) for a given x value
    return pow(x, 1.5)

if __name__ == '__main__':
    #n=2^k
    #Ask user for a k input, and print the return value of simpsonsRule(n)
    k = int(input("Enter k, where n=2^k"))
    print(simpsonsRule(pow(2,k)))