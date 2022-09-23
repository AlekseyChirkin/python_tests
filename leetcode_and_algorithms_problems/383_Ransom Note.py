import collections

ransomNote = "aa"
magazine = "aab"


class Solution:
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        # first solving:

        # for ch in ransomNote:
        #     if ransomNote.count(ch) > magazine.count(ch):
        #         return False
        # return True

        #       second solving:

        #         magazine_dict = {}

        #         for ch in magazine:
        #             if ch in magazine_dict:
        #                 magazine_dict[ch] += 1
        #             else:
        #                 magazine_dict[ch] = 1

        #         for ch in ransomNote:
        #             if ch in magazine_dict:
        #                 magazine_dict[ch] -= 1
        #                 if magazine_dict[ch] < 0:
        #                     return False
        #             else:
        #                 return False

        #         return True

        # third solving:

        return not collections.Counter(ransomNote) - collections.Counter(magazine)


print(Solution.canConstruct(ransomNote, magazine))
