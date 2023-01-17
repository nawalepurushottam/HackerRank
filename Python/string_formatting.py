def decimalToBinary(n):
    x=1
    ans=0
    while x<=n:
        x*=2
    x=x/2
    
    while x>0:
        lastDigit=int(n/x)
        n=int(n-lastDigit*x)
        x=int(x/2)
        ans=ans*10+lastDigit
    return str(ans)


def decimalToOctal(n):
    x=1
    ans=0
    while x<=n:
        x*=8
    x/=8
    while x>0:
        lastDigit=int(n/x)
        n-=int(lastDigit*x)
        x=int(x/8)
        ans=ans*10+lastDigit
    return str(ans)

def decimalToHexdecimal(n):
    x=1
    ans=""
    while x<=n:
        x*=16
    x/=16
    while x>0:
        lastDigit=int(n/x)
        n-=int(lastDigit*x)
        x=int(x/16)

        if lastDigit<=9:
            ans=ans+str(lastDigit)
        else:
            ans=ans+chr(65+lastDigit-10)
    return str(ans)

def print_formatted(n):
    width=len(decimalToBinary(n))
    for i in range(1,n+1):
        print(str(i).rjust(width),decimalToOctal(i).rjust(width),decimalToHexdecimal(i).rjust(width),decimalToBinary(i).rjust(width))

if __name__=='__main__':
    n=int(input())
    print_formatted(n)
    





