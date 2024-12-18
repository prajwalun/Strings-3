# The numberToWords method converts a number into its English word representation.

# Handle the special case for zero by returning "Zero".
# Process the number in groups of 3 digits (thousands, millions, billions).
# - Use a helper method to convert each 3-digit group to words.
# - Append the appropriate big number suffix (e.g., Thousand, Million) for each group.
# - Combine results, stripping extra spaces.

# The numberToWordsHelper method converts a 3-digit number to words.
# - Handle hundreds, tens, and ones separately.
# - Use pre-defined lists for digits, teens, and tens for conversion.

# TC: O(log n) - Each group of 3 digits is processed once.
# SC: O(log n) - Space for the recursive calls based on the number of groups.


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        bigString = ["Thousand", "Million", "Billion"]
        result = self.numberToWordsHelper(num % 1000)
        num //= 1000
        
        for i in range(len(bigString)):
            if num > 0 and num % 1000 > 0:
                result = self.numberToWordsHelper(num % 1000) + bigString[i] + " " + result
            num //= 1000
        
        return result.strip()

    def numberToWordsHelper(self, num: int) -> str:
        digitString = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teenString = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tenString = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        result = ""
        if num > 99:
            result += digitString[num // 100] + " Hundred "
        
        num %= 100
        if num < 20 and num > 9:
            result += teenString[num - 10] + " "
        else:
            if num >= 20:
                result += tenString[num // 10] + " "
            num %= 10
            if num > 0:
                result += digitString[num] + " "
        
        return result