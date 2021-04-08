def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    elif type(value) == list:
        the_mean = sum(value) / len(value)
    else:
        return "inocrrect type"
    return the_mean


mean_list =  [2, 4, 6]
mean_dict = {"a": 2, "b": 4, "c": 6}

print(mean(mean_list))
print(mean(mean_dict))
print(mean(2))
