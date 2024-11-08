class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        if l == 1:
            return True
        else:
            s = s.lower()
            i = 0
            j = l - 1
            c1 = s[i]
            c2 = s[j]
            f1 = c1.isalnum()
            f2 = c2.isalnum()
            result = True
            while(i < j):
                if f1 and f2:
                    if c1 == c2:
                        i = i + 1
                        j = j - 1
                        c1 = s[i]
                        c2 = s[j]
                        f1 = c1.isalnum()
                        f2 = c2.isalnum()
                        continue
                    else:
                        result = False
                        break
                elif f1 and not f2:
                    j = j - 1
                    c2 = s[j]
                    f2 = c2.isalnum()
                    continue
                elif not f1 and f2:
                    i = i + 1
                    c1 = s[i]
                    f1 = c1.isalnum()
                    continue
                else:
                    i = i + 1
                    j = j - 1
                    c1 = s[i]
                    c2 = s[j]
                    f1 = c1.isalnum()
                    f2 = c2.isalnum()
                    continue
            return result
