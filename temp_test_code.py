def has_duplicates(arr):
    """
    检测数组中是否有重复的元素。

    Args:
        arr (list): 输入的数组。

    Returns:
        bool: 是否有重复的元素。
    """
    # 通过集合来检测 duplicates
    return len(arr) != len(set(arr))

# 测试例子
arr1 = [1, 2, 3, 4, 5]
print(has_duplicates(arr1))  # 输出：False

arr2 = [1, 2, 3, 3, 5]
print(has_duplicates(arr2))  # 输出：True

