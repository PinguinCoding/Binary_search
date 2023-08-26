def binary_search(_list, elem):
    idx_mid = len(_list) // 2
    mid = _list[idx_mid]
    print(f"Middle value index: {idx_mid}")
    print(f"Middle value: {mid}")
    print(_list)

    if len(_list) == 1:
        if mid == elem:
            return mid
        return print("Element not found it.")

    if mid == elem:
        return mid
    elif mid > elem:
        half_list = _list[:idx_mid]
        print(half_list)
        print("=====")
        return binary_search(half_list, elem)
    elif mid < elem:
        half_list = _list[idx_mid+1:]
        print(half_list)
        print("=====")
        return binary_search(half_list, elem)


lista = [3, 9, 17, 21, 28, 50, 66, 84, 87, 92]
elemento = int(input("Input element: "))
print(binary_search(lista, elemento))
