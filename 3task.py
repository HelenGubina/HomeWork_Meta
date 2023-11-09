def str_rev(str_par):
    if len(str_par) > 0:
        str_r = str_par[len(str_par)-1] + str_rev(str_par[0:len(str_par)-1])
        return str_r
    else:
        return ""


print(str_rev("Happy"))
