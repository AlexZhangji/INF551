def parse_data(fname):
    with open(fname) as f:
        # assume only two lines
        text_list = f.readlines()
        return int(text_list[0]), text_list[1]


def f_scan(head_pos_, pos_queue_):
    path = []
    if len(pos_queue_) == 0:
        # print path
        return path

    # if two has same distance, head will move to inner most stack
    # TODO fix the same distance issue
    next_head = min(pos_queue_, key=lambda x: abs(x - head_pos_))

    # break the list to two parts, first iterate the one
    cur_head_index = pos_queue_.index(next_head)
    path = pos_queue_[cur_head_index:] + list(reversed(pos_queue_[:cur_head_index]))
    return path


def print_result(res_path, head_pos_):
    tot_cost = abs(head_pos_ - res_path[0])
    for i in range(len(res_path) - 1):
        tot_cost += abs(res_path[i] - res_path[i + 1])

    res_path_str = ','.join(str(x) for x in res_path)
    print res_path_str, '\n', tot_cost, '\n', '{},{}'.format(res_path[-1], tot_cost)


# fname = sys.argv[1:][0]

fname = 'test1.txt'
head_pos, raw_pos_queue = parse_data(fname)
# print head_pos, pos_queue

pos_queue = sorted([int(num) for num in raw_pos_queue.split(',')])
# if pos_queue does not has 199, add to it
if 199 not in pos_queue:
    pos_queue.append(199)

result_path = f_scan(head_pos, pos_queue)
print_result(result_path, head_pos)
