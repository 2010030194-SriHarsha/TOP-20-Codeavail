def digitsToWords(n,forms):
    if n==0:
        return
    rem=n%10
    n=n//10
    digitsToWords(n,forms)
    print(forms[rem],end=" ")
n=int(input())
forms=['zero','one','two','three','four','five','six','seven','eight','nine']
digitsToWords(n,forms)