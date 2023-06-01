def find_singleton_item(list):
    count_dict = {}
    
    for item in list:
        count_dict[item] = count_dict.get(item, 0) + 1

    for item, count in count_dict.items():
        if count == 1:
            return item
    return None


my_list = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_singleton_item(my_list))