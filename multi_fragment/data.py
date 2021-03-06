if_1 = 0
if_2 = 0
if_3 = 0
if_4 = 0

def diff(a, b):
    b = set(b)
    return [aa for aa in a if aa not in b]

def compare_two_list_ingore_order(lst1, lst2):
    for item in lst1:
        if item not in lst2:
            return False
    return True

def min_of_two_digit_list(lst, roads_visited, allow_hamilton=None):

    x = 0
    y = 0
    value = 999999999999
    for i, item in enumerate(lst):
        for j, item1 in enumerate(item):
            if item1 and item1 < value and check_if_roads_is_correct([i, j], roads_visited, allow_hamilton):
                value = item1
                x = i
                y = j
    print 'min', value
    return {
        'value': value,
        'index_x': x,
        'index_y': y
    }

def check_if_roads_is_correct(road, roads_visited, allow_hamilton):
    if road in roads_visited or road[::-1] in roads_visited: # czy ta sciezka juz byla
        return False
    elif road[0] in [road_visited[0] for road_visited in roads_visited]: # czy juz stad nie jechal
        return False
    elif road[1] in [road_visited[1] for road_visited in roads_visited]: #  czy juz dotad nie jechal
        return False

    elif not allow_hamilton and roads_visited and compare_two_list_ingore_order([road_visited[0] for road_visited in roads_visited], [road_visited[1] for road_visited in roads_visited]):
        return False

    else:
        return True


def get_road(distances):



    total_distance = 0

    roads_visited = []

    for i in range(len(distances)-1):
        _roads_visited = list(roads_visited)  # copy
        _distances = list(distances)  # clone
        while True:  # i love you
            min_distances = min_of_two_digit_list(_distances, _roads_visited)
            shortest_path = min_distances['value']
            x_index = min_distances['index_x']  # from
            index_y = min_distances['index_y']  # to
            if 1:  # TODO
                total_distance += shortest_path
                roads_visited.append([x_index, index_y])
                break
            else:
                _roads_visited.append([x_index, index_y])

    last_road = min_of_two_digit_list(distances, roads_visited, True)
    roads_visited.append([last_road['index_x'], last_road['index_y']])
    total_distance += last_road['value']
    print if_1, if_2, if_3, if_4
    return total_distance
