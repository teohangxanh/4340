# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 07:23:49 2020

@author: Teo
"""

'''
Usage: Return the index in text where pattern = substring of text
'''

import timeit

def brute_force(p, t):
    result = []
    i = 0
    while i <= len(t) - len(p):
        j = 0
        count = 0
        if t[i: i + len(p)] == p:
            result.append(i)
        i += 1
    return result

def rb(p, t):
    p = p.lower()
    t = t.lower()
    result = []
    mod = 2 ** 20
    hash_value = 0
    for i in range(len(p)):
        hash_value += (ord(p[i]) * (len(p) ** (len(p) - i - 1)) % mod) % mod
    i = 0
    h = 0
    while i <= len(t) - len(p):
        # Compute hash value of text
        if i == 0:
            for j in range(len(p)):
                h += (ord(t[j]) * (len(p) ** (len(p) - j - 1)) % mod) % mod
        if i > 0:
            head = ord(t[i - 1]) * (len(p) ** (len(p) - 1))
            h = (((h - head) * len(p)) % mod + ord(t[i + len(p) - 1])) % mod
        if hash_value == h and t[i: i + len(p)] == p:
            result.append(i)
        i += 1
    return result  

def bm(p, t):
    result = []
    i = 0
    while i <= len(t) - len(p):
        if t[i: i + len(p)] == p:
            result.append(i)
            i += 1
        else:
            last_char_index = i + len(p) - 1
            last_char  = t[last_char_index]
            # Find the closest same char in pattern from the right
            if last_char in p:
                i = last_char_index
            else:
                i = last_char_index + 1
    return result

# Return length of the prefix / suffix and shift amount)
def lps(p):
    result = [0] * len(p)
    i = 0
    j = 1
    while j < len(p):
        if p[i] == p[j]:
            result[j] = result[j - 1] + 1
            i += 1
            j += 1
            continue
        if p[i] != p[j]:
            i = 0
        j += 1
    count = 0
    for x in range(len(result)):
        if result[x] > 0:
            count += 1
        elif result[x] == 0 and count > 0:
            return count, x - count
    # return result

def kmp(p, t):
    if lps(p) != None:
        shamt, length = lps(p)
        result = []
        i = 0
        while i <= len(t) - len(p):
            if p == t[i: i + len(p)]:
                result.append(i)
                i += 1
            else:
                if p[shamt: shamt + length] == t[i + shamt: i + shamt + length]:
                    i += shamt
                else:
                    i += 1
        return result
    else:
        return brute_force(p,t)
    
        
text = "String matching is something crucial for database development and text processing software.Fortunately, every modern programming language and library is full of functions for string processing that help us in our everyday work. However it's important to understand their principles.String algorithms can typically be divided into several categories. One of these categories is string matching."
pattern = 'in'
print(brute_force(pattern, text))
print(rb(pattern, text))
print(bm(pattern, text))
print(kmp(pattern, text))

# '''Check the running time of all algorithms'''
print(format(timeit.timeit('''def brute_force(p, t):
    result = []
    i = 0
    while i <= len(t) - len(p):
        j = 0
        count = 0
        if t[i: i + len(p)] == p:
            result.append(i)
        i += 1
    return result
text = "String matching is something crucial for database development and text processing software.Fortunately, every modern programming language and library is full of functions for string processing that help us in our everyday work. However it's important to understand their principles.String algorithms can typically be divided into several categories. One of these categories is string matching."
pattern = "in"''', number = 1000), 'e'))

print(format(timeit.timeit('''def rb(p, t):
    result = []
    mod = 2 ** 20
    hash_value = 0
    for i in range(len(p)):
        hash_value += ((ord(p[i]) - ord('a')) * (len(p) ** (len(p) - i - 1)) % mod) % mod
    i = 0
    h = 0
    while i <= len(t) - len(p):
        # Compute hash value of text
        if i == 0:
            for j in range(0, len(p)):
                h += ((ord(t[j]) - ord('a')) * (len(p) ** (len(p) - j - 1)) % mod) % mod
        if i > 0:
            h = ((len(p) * h) - (ord(t[j-1]) - ord('a')) * (len(p) ** (len(p) - 1)) + ord(t[j + len(p) - 1]) - ord('a')) % mod
        if hash_value == h and t[i: i + len(p)] == p:
            result.append(i)
        i += 1
    return result  ''', number = 1000), 'e'))

print(format(timeit.timeit('''def bm(p, t):
    result = []
    i = 0
    while i <= len(t) - len(p):
        if t[i: i + len(p)] == p:
            result.append(i)
            i += 1
        else:
            last_char_index = i + len(p) - 1
            last_char  = t[last_char_index]
            # Find the closest same char in pattern from the right
            if last_char in p:
                i = last_char_index
            else:
                i = last_char_index + 1
    return result''', number = 1000), 'e'))

print(format(timeit.timeit('''def lps(p):
    result = [0] * len(p)
    i = 0
    j = 1
    while j < len(p):
        if p[i] == p[j]:
            result[j] = result[j - 1] + 1
            i += 1
            j += 1
            continue
        if p[i] != p[j]:
            i = 0
        j += 1
    count = 0
    for x in range(len(result)):
        if result[x] > 0:
            count += 1
        elif result[x] == 0 and count > 0:
            return count, x - count
    # return result

def kmp(p, t):
    if lps(p) != None:
        shamt, length = lps(p)
        result = []
        i = 0
        while i <= len(t) - len(p):
            if p == t[i: i + len(p)]:
                result.append(i)
                i += 1
            else:
                if p[shamt: shamt + length] == t[i + shamt: i + shamt + length]:
                    i += shamt
                else:
                    i += 1
        return result
    else:
        return brute_force(p,t)''', number = 1000), 'e'))