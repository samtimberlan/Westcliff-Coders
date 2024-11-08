class Solution:
    def romanToInt(self, roman_str: str) -> int:
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "Z": 0
        }
        result = 0
        # Add sentinel value 'Z' to handle last character
        roman_str = roman_str + 'Z'
        
        for i in range(len(roman_str)-1):
            current_value = roman_values[roman_str[i]]
            next_value = roman_values[roman_str[i+1]]
            
            if current_value < next_value:
                result -= current_value
            else:
                result += current_value
                
        return result
    
# Bounded up to 3999
# Time complexity: O(1)
# Space complexity: O(1)