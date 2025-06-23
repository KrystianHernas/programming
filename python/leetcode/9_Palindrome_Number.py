# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        list_of_digits = [i for i in str(x)]
        even_length = len(list_of_digits)/2
        odd_length = (len(list_of_digits)-1)/2
        print(len(list_of_digits))
        # parzyste
        if len(list_of_digits) % 2 == 0:
            for i in range(0, even_length):
                if list_of_digits[i] != list_of_digits[len(list_of_digits)-1-i]:
                    return False
        # nieparzyste
        else:
            for i in range(0, odd_length):
                if list_of_digits[i] != list_of_digits[len(list_of_digits)-1-i]:
                    return False
        return True
        """
        :type x: int
        :rtype: bool
        """

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
x = 121
print(Solution().isPalindrome(x))

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
x = -121
print(Solution().isPalindrome(x))

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
x = 10
print(Solution().isPalindrome(x))