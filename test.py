arb_list = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, [375, [500, 505]]]], 0, ['{slice, owned}'], 22]

def dummy_func(list_thing):
    container = []
    for item in list_thing:
        if isinstance(item, list):
            cont2 = (dummy_func(item))
            for item2 in cont2:
                container.append(item2)
        else:
            container.append(item)
    return container

a = dummy_func(arb_list)
for item in a:
    print(item)