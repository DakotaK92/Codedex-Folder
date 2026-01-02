grocery_list = {'apple', 'banana', 'orange'}
friends_list = {'pears', 'kiwi', 'grapes'}

union_result = grocery_list | friends_list
intersection_result = grocery_list & friends_list
difference_result = grocery_list - friends_list

print('Union:', union_result)
print('Intersection:', intersection_result)
print("My Fruits - Friend's Fruits:", difference_result)