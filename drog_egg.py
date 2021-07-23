FLOOR_COUNT = 100

def drop_egg(break_point):
    min_floor = 0
    step_size = 14
    max_floor = step_size

    while(max_floor < FLOOR_COUNT):
        if max_floor >= break_point:
            for i in range(min_floor, max_floor):
                if i >= break_point:
                    return i - 1
        else:
            min_floor = max_floor + 1
            max_floor = max_floor + step_size - 1
            step_size = step_size - 1

    if min_floor >= break_point:
        return min_floor - 1
    else:
        return FLOOR_COUNT

print("For break_point 1 answer is: " + str(drop_egg(1)))
print("For break_point 100 answer is: " + str(drop_egg(100)))
print("For break_point 101 answer is: " + str(drop_egg(101)))
print("For break_point 61 answer is: " + str(drop_egg(61)))