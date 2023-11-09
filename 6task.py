def depth(list_par):
    list_included = False
    for i in list_par:
        if isinstance(i, list):
            list_included = True
            depth_l = depth(i) + 1
            return depth_l
    if not list_included:
        return 1


print(depth([1, [2, [3, [4, [5]]]]]))
