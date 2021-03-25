from collections import deque

def palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

if __name__ == '__main__':
    print(palindrome('a')) # True
    print(palindrome('racecar')) # True
    print(palindrome('')) # True
    print(palindrome('radar')) # True
    print(palindrome('halibut')) # False