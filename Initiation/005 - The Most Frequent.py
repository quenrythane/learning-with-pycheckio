# https://py.checkio.org/en/mission/the-most-frequent/
"""
https://py.checkio.org/en/mission/the-most-frequent/
"""


def most_frequent(data: list) -> str:
    my_dict = {}
    for i in data:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    highest = [0, '']
    for k, v in my_dict.items():
        if v > highest[0]:
            highest = [v, k]

    return highest[1]


def most_frequent2(data: list) -> str:
    import pandas as pd
    df = pd.DataFrame(data, columns=['valeurs'])
    dg = df['valeurs'].value_counts()
    return dg.index[0]


def most_frequent3(data: list) -> str:
    total = 0
    most = data[0]
    for i in data:
        if data.count(i) > total:
            most = i
            total = data.count(i)
        elif data.count(i) == total:
            if i < most:
                most = i
                total = data.count(i)
    return most


data1 = ['a', 'a', 'bi', 'bi', 'bi']
print(data1[0])
print(most_frequent(data1))
print(most_frequent2(data1))
print(most_frequent3(data1))
