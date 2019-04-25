def print_items(container):
    if len(container) == 0:
        print(" Hey, there are no items here!")
    else:
        for i in container:
            print(('  {}').format(i))
