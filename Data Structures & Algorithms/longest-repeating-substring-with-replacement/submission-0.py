## like the opposite of a set, want ONLY duplicates/repeating characters!
## i forgot to include using k... but lets try now
## after using chatgpt to guide: gotta track length and frequency of most counted letter
## then later compare ferquency and k and make decision(?)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1
        curr_length = 1
        left = 0
        right = 0

        frequent = {} ## key of letter, value of frequency

        while right < len(s):
            if s[right] not in frequent:
                frequent[s[right]] = 0
            frequent[s[right]] += 1 ## increment value if exists
            length = right - left + 1
            max_freq = max(frequent.values())

            if (length - max_freq) > k: ## not enough replacements
                frequent[s[left]] -= 1
                left += 1
                right += 1
                length -= 1

            else: ## enough replacements
                longest = max(longest, length)
                right += 1
        return longest

            



        # while right < len(s)
        ## could compare curr (right) vs prev (left)
        # if curr == prev: string is continuing
            # curr += 1
        ## if curr != prev: string has broken, no more duplicates
            ## prev = curr -> think greedy alg, the letters between are useless regardless
            ## prev += 1

