import time
import collections

def isPalindrome(s: str) -> bool:
    # strs = []
    # for char in s:
    #     if char.isalnum():
    #         strs.append(char.lower())

    # while len(strs) > 1:
    #     if strs.pop(0) != strs.pop():
    #         return False
    # b = len(strs)
    # for idx in range(0, b//2):
    #     if strs[idx] != strs[b-idx-1]:
    #         return False

    # strs: Deque = collections.deque()
    #
    # for char in s:
    #     if char.isalnum():
    #         strs.append(char.lower())
    #
    # while len(strs) > 1:
    #     if strs.popleft() != strs.pop():
    #         return False
    #
    # return True

    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]

a = input()
start = time.time()
for i in range(10000):
    isPalindrome(a)
end = time.time()
print(f"{end - start:.5f} sec")
print(isPalindrome(a))