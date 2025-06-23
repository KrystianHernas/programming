# Data structures
# Arrays (Lists in Python)
# Slicing
from collections import deque
from itertools import permutations
arr, start, end = [], 0, 0
arr[start:end]
# list comprehension
[x**2 for x in arr]
# prefix sum - technika pozwalająca na szybkie obliczanie sumy elementów w podanym zakresie tablicy
# Inicjalizujemy o jeden więcej element niż array
prefix_sum = [0] * (len(arr) + 1)
for i in range(len(arr)):
    # sumę poprzednich przechowujemy w następnym elemencie
    prefix_sum[i + 1] = prefix_sum[i] + arr[i]
# Hashing (dicts and sets)
# Jak zliczyć częstotliwość występowania elemetów w tablicy?
freq, nums = {}, [1, 2, 3]
for num in nums:
    freq[num] = freq.get(num, 0) + 1
# Sprawdzenie duplikatów
seen = set()
for num in nums:
    if num in seen:
        print("Duplicate found!")
    seen.add(num)
# Linked list
# odwrócenie listy to najłatwiej przy użyciu slicingu czyli normalnie jak lista tylko dodanie step -1 co powoduje rozpoczęcie od ostatniego elementu
head = list[::-1]
# stos
stack = []
stack.append(1)  # Push
stack.pop()      # Pop
# kolejki
queue = deque()
queue.append(1)   # Enqueue
queue.popleft()   # Dequeue
# drzewo - inorder traversal to sposób na ziterowanie po wszystkich elementach drzewa


def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val)
        inorder_traversal(node.right)
# Są jeszcze
# Preorder Traversal, gdzie najpierw odwiedzamy root, potem lewe/prawe


def preorder_traversal(node):
    if node:
        print(node.val)
        preorder_traversal(node.left)
        preorder_traversal(node.right)
# albo Postorder Traversal czyli na końcu root


def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.val)

# i jeśli zamienimy kolejnością left z right to wyjdą wersje reverse tych trzech traversali
# Jest jeszcze trzeci rodzaj, gdzie przechodzimy poziom po poziomie (BFS - Breadth-first search)


def level_order_traversal(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
# albo coś takiego


def bfs(graph, start):
    # startujem z root node i dodajemy do kolejki
    queue = deque([start])
    visited = set()
    while queue:
        # dekolejkujemy, następuje odwiedzenie node
        node = queue.popleft()
        # jeśli są, dodajemy jego dzieci do kolejki
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])


# Pythonic Algorithms
# Sorting
arr = [3, 1, 4]
sorted_arr = sorted(arr)
# or python implementation of quicksort algorithm


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    # wybór elementu środkowego zaokrąglonego w dół
    pivot = arr[len(arr) // 2]
    # podział arr na 3 podarraye
    # mniejsze od pivota
    left = [x for x in arr if x < pivot]
    # równe pivotowi
    middle = [x for x in arr if x == pivot]
    # większe od pivota
    right = [x for x in arr if x > pivot]
    # rekurencyjne sortowanie prawego i lewego arraya
    return quicksort(left) + middle + quicksort(right)


# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print("Sorted array is:", sorted_arr)

# searching


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target)
print(f"Element found at index: {result}")  # Output: Element found at index: 4

# memoizacja - polega na tym, by nie obliczać wielokrotnie tych samych wartości,
# lecz by zapisywać wyniki już obliczonych podproblemów (przykład bazowy to ciąg fibonacciego)


def fib(n):
    # jeśli mniejsza od jedynki to nie sumujemy
    if n <= 1:
        return n
    # każda kolejna liczba to suma dwóch poprzednich
    return fib(n-1) + fib(n-2)
# Jako, że mamy wykładniczą złożoność czasową O(2**n), optymalizujemy poprzez zapisywanie każdego obliczonego podproblemu


def fib(n, memo={}):
    if n <= 1:
        return n
    # wprowadzenie słownika memo, w którym zapisujemy wyniki każdego z podproblemów dzięki odwijaniu funkcji
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


# Przykład użycia
print(fib(10))  # Wynik: 55

# string manipulation
# reverse string
s = 'fds'
reversed_str = s[::-1]
# palindrome check
is_palindrome = s == s[::-1]

# sprawdzic unikalność stringa, albo w sumie każdego zbioru pewnie


def is_unique(string):
    return len(set(string)) == len(string)

# permutacje - sprawdzenie czy jedna tablica znaków jest permutacją innej.
# można to zrobić poprzez porównanie posortowanych wersji obu ciągów


def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


# brudnopis
print("Brudnopis")
nums = [4, 3, 2, 7, 8, 3, 2, 1]
# set(nums)
s = set(nums)
for k, v in enumerate(s):
    print(k, "v", v)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2}
value_to_find = 4
# Find the keys associated with the value
keys_with_value = [key for key,
                   value in my_dict.items() if value == value_to_find]
print(keys_with_value)

def findSubstring(s: str, words: list[str]) -> list[int]:
    # długość substringa stworzonego z wszystkich stringów w words
    # len(words)*len(words[0])
    permutacje = list(permutations(words))
    st = ""
    for p in range(len(permutacje)):
        for sp in permutacje[p]:
            st += sp
        permutacje[p] = st
        st = ""
    print(permutacje)
    index = 0
    l = len(words)*len(words[0])
    res = []
    while index < len(s):
        if s[index:l + index] in permutacje:
            res.append(index)
        index += 1
    return res

s = "fffffffffffffffffffffffffffffffff"
words = ["a","a","a","a","a","a","a","a","a","a","a"]
r = findSubstring(s=s,words=words)
print(r)