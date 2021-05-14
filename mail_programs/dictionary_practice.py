# Get the key of a minimum value from the following dictionary

def func(dictionary):
    values = list(dictionary.values())
    keys = list(dictionary.keys())
    sorted_values = values.copy()
    sorted_values.sort()
    # print(values)
    # print(sorted_values)
    key_index = values.index(sorted_values[0])
    minimum_value_key = keys[key_index]
    print("MINIMUM VALUE IN THE DICTIONARY IS OF KEY : \"" + minimum_value_key + "\"")


sampleDict = {'Physics': 82, 'Math': 65, 'history': 75}

func(sampleDict)
