from functools import reduce

domain = [1, 2, 3, 4 ,5]

#f(x) = x * 2
our_range = map(lambda num: num * 2, domain)
print(list(our_range))

#filter numbers divisible by 2 without a remainder from the domain
evens = filter(lambda num: num % 2 == 0, domain)
print(list(evens))

#this reduce() has an initial value of 0
the_sum = reduce(lambda acc, num: acc + num, domain, 0)
print(the_sum)

###sorted() ---> arranges orderly starting with uppercase letters
words = ['Boss', 'a', 'Alfred', 'Major league', 'system', 'drop']
print("Sorting by default")
print(sorted(words))

#sorting starting with lowercase
print("Sorting with a lambda key")
print(sorted(words, key = lambda s: s.lower()))

##### 'this string'.lower() ===== str.lower('this string')
print("Sorting with a method")
words.sort(key= str.lower, reverse = True)
print(words)