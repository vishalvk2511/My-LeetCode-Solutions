class Solution:
    def isPalindrome(self, x: int) -> bool:
       
        sign = 1

        rev_Num = 0

        if x < 0 :
            return False

        x_c = x
        while x:
            digit = x%10

            rev_Num = rev_Num * 10 + digit

            x = x//10

        if x_c == rev_Num:
            return True
        else:
            return False
        

            
            

    