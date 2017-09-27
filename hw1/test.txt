import sys


def parse_data(fname):
    with open(fname) as f:
        # assume only two lines
        text_list = f.readlines()
        return int(text_list[0]), text_list[1]


def get_closest_num(pos_head_, pos_queue_):
    closest_pos = []
    least_distance = sys.maxint

    for pos in pos_queue_:
        distance = abs(pos_head_ - pos)
        if distance < least_distance or distance == least_distance and pos < closest_pos:
            least_distance = distance
            closest_pos = pos

    return closest_pos


def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val], [value for value in the_list if value == val]


def scan(head, queue):
    path = []
    next_head = get_closest_num(head, queue)
    extra = 0  # use to track path cost for 0 and 199 added

    if head > max([num for num in queue]):
        return list(reversed(queue)), 0
    if head < min([num for num in queue]):
        return queue, 0

    # handle the possibility that multiple num in list is the same as the head
    if next_head == head:
        # remove all equal head from the list
        queue, head_list = remove_values_from_list(queue, head)
        path += head_list
        next_head = get_closest_num(head, queue)

    go_right = head < next_head
    cur_head_index = queue.index(next_head)
    if go_right:
        extra += (199 - queue[-1]) * 2
        path += queue[cur_head_index:] + list(reversed(queue[:cur_head_index]))

    else:
        extra = queue[0] * 2
        path += list(reversed(queue[:cur_head_index + 1])) + queue[cur_head_index + 1:]

    return path, extra

    # fname = 'test1.txt'


if sys.argv[1:]:
    fname = sys.argv[1:][0]
    # fname = 'test1.txt'

    head_pos, raw_pos_queue = parse_data(fname)
    pos_queue = sorted([int(num) for num in raw_pos_queue.split(',')])
    origin_queue = pos_queue[:]

    result_path, extra = scan(head_pos, pos_queue)

    tot_cost = abs(head_pos - result_path[0]) + extra
    for i in range(len(result_path) - 1):
        tot_cost += abs(result_path[i] - result_path[i + 1])

    res_path_str = ','.join(str(x) for x in result_path)
    print res_path_str, '\n', tot_cost, '\n', '{},{}'.format(result_path[-1], tot_cost)
