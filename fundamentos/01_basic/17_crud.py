# CRUD: Create, Read, Update & Delete

numbers = [1,2,3,4,5] # List
print(numbers[1]) # Show 1st item
numbers[-1]=10 # Modify last item
print(numbers)

numbers.append(70) # Add item to end of list
print(numbers)

numbers.insert(0,'hello') # Insert at top of list
print(numbers)

numbers.insert(3,'change') # Add at position 3
print(numbers) # out: ['hola', 1, 2, 'change', 3, 4, 10, 70]

tasks = ['todo 1','todo 2','todo 3']
new_list= numbers + tasks # Merging 2 lists
print(new_list)

index = new_list.index('todo 2')
print('position: ',index)
new_list[index]='todo changed' # update position 9
print(new_list)

new_list.remove('todo 1') # Remove or delete especific item
print(new_list)

new_list.pop() # Delete the last item in the list.
print(new_list)

new_list.pop(0) # Delete position [0]
print(new_list)


new_list.reverse() # Change position to reverse list - [reverse]
print(new_list)

numbers_2 = [1,4,6,3]
numbers_2.sort() # sort list
print(numbers_2)

strings=['re','ab','ed']
strings.sort() # ordering text string
print(strings)