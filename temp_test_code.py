def has_duplicates(arr):
    """
    ����������Ƿ����ظ���Ԫ�ء�

    Args:
        arr (list): ��������顣

    Returns:
        bool: �Ƿ����ظ���Ԫ�ء�
    """
    # ͨ����������� duplicates
    return len(arr) != len(set(arr))

# ��������
arr1 = [1, 2, 3, 4, 5]
print(has_duplicates(arr1))  # �����False

arr2 = [1, 2, 3, 3, 5]
print(has_duplicates(arr2))  # �����True

