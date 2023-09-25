def main(S,d):
    a=(S-d**2)/(2*d)
    b=a+d
    x=b-a*a/(2*b)
    return(x)
print(main(26,5))