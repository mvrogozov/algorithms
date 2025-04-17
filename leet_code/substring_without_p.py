class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        result = 0
        length = 0
        for index in range(len(s)):
            for sign in s[index:]:
                if sign in letters:
                    letters = set()
                    length = 0
                    break
                else:
                    letters.add(sign)
                    length += 1
                    if length > result:
                        result = length
        return result


def main():
    a = Solution()
    string = 'assbest'
    print(a.lengthOfLongestSubstring(string))

if __name__ == '__main__':
    main()