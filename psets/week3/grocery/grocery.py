g_list = {}

while True:
    try:
        item = input()
        if item in g_list:
            g_list[item] += 1
        else:
            g_list[item] = 1
    except EOFError:
        for i in sorted(g_list):
            print(g_list[i],i.upper())
        break
    else:
        pass

