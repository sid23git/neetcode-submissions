class Solution:
    def isPalindrome(self, s: str) -> bool:

            L = 0 
            R = len(s) -1 

            while L < R:


                while L < R and not s[L].isalnum():
                    L += 1

            # Skip non alphanumeric from RIGHT
                while L < R and not s[R].isalnum():
                    R -= 1

                # Compare
                if s[L].lower() != s[R].lower():
                    return False  # Your answer!

                # Move both inward
                L += 1  # Your answer!
                R -=1  # Your answer!
 

            return True 

