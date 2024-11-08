class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
		//Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        //Reverse
		for i in range(n):
            for j in range(n // 2):
                matrix[i][n - j - 1], matrix[i][j] = matrix[i][j], matrix[i][n - j - 1]

    # Time complexity O(number of cells)
    # Space complexity O(1)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i,c in enumerate(strs[0]):
            for s in strs:
                if i >= len(s) or s[i] != c:
                    return strs[0][:i]
        return strs[0]

    # Time complexity O(sum of all characters in all strings)
    # Space complexity O(1)
