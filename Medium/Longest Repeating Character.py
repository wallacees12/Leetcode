class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_count = 0
        char_count = {}
        start = 0

        for end in range(len(s)):
            char = s[end]
            #Store a ditionary of how many times character appears  
            char_count[char] = char_count.get(char, 0) + 1
            max_count = max(max_count, char_count[char])

            # If the window size minus the max frequency exceeds k, shrink the window
            while (end - start + 1) - max_count > k:
                char_count[s[start]] -= 1
                start += 1

            # Update the maximum length of the window
            max_len = max(max_len, end - start + 1)

        return max_len
