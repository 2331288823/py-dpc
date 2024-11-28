
def list_count(item: list, data_list: list) -> dict:
    counts = {}
    for listItem in data_list:
        if listItem in item:
            counts[listItem] = counts.get(listItem, 0) + 1
    return counts


def list_sort(data_list: list) -> list:
    # 列表
    data_list.sort(key=lambda x: x[1], reverse=True)
    return data_list
