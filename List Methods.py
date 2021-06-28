# append
animals = ['cat', 'dog', 'rabbit']
animals.append('guinea pig')
print('Updated animals list: ', animals)

# Extend
languages = ['French', 'English']
languages1 = ['Spanish', 'Portuguese']
languages.extend(languages1)
print('Languages List:', languages)

# Insert
vowel = ['a', 'e', 'i', 'u']
vowel.insert(3, 'o')
print('Updated List:', vowel)

# remove
animals = ['cat', 'dog', 'rabbit', 'guinea pig']
animals.remove('rabbit')
print('Updated animals list: ', animals)

# Count
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
count = vowels.count('i')
print('The count of i is:', count)
count = vowels.count('p')
print('The count of p is:', count)

# pop
languages = ['Python', 'Java', 'C++', 'French', 'C']
return_value = languages.pop(3)
print('Return Value:', return_value)
print('Updated List:', languages)

# Reverse
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)
systems.reverse()
print('Updated List:', systems)

# Sort
vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort()
print('Sorted list:', vowels)

# Copy
old_list = [1, 2, 3]
new_list = old_list
new_list.append('a')
print('New List:', new_list)
print('Old List:', old_list)

#Clear
list = [{1, 2}, ('a'), ['1.1', '2.2']]
list.clear()
print('List:', list)