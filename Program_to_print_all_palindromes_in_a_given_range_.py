def isPalindrome(n: int) -> bool:
 
    
    rev = 0
    i = n
    while i > 0:
        rev = rev * 10 + i % 10
        i //= 10
 
    
    return (n == rev)
 
def countPal(minn: int, maxx: int) -> None:
    for i in range(minn, maxx + 1):
        if isPalindrome(i):
            print(i, end = " ")
 
if __name__ == "__main__":
    countPal(int(input()),int(input()))
    
 