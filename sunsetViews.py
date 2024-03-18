def sunsetViews(buildings, direction):
    indices_with_views = []
    start_index = 0 if direction == 'WEST' else len(buildings) - 1
    step = 1 if direction == 'WEST' else -1

    current_max_height = 0
    index = start_index

    while 0 <= index < len(buildings):
        if buildings[index] > current_max_height:
            indices_with_views.append(index)
            current_max_height = buildings[index]
        index += step

    if direction == 'EAST':
        indices_with_views.reverse()
    
    return indices_with_views
