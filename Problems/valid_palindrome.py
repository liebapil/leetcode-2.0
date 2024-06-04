class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""# we are making a new string which is removing all the non numeric stuff 
        for c in s: # iterate throough each letter in s 
            if c.isalnum(): #python has a built in function if its numeric if it is 
                newStr += c.lower() #then we awant to includ it to the new string but we want to make all charcters lower case and then we ahve the new string 
        return newStr == newStr[::-1]# here we wqnt to see if its the same as reverse which is the sytax for seeing if its the same is foward and backwards 
         

