import copy


def parse_data(fname):
    with open(fname) as f:
        # assume only two lines
        text_list = f.readlines()
        return int(text_list[0]), text_list[1]


def sstf(head_pos_, pos_queue_, path=[]):
    # get closest number for head_pos in the list
    # print 'pos queue: {}'.format(pos_queue_)
    if len(pos_queue_) == 0:
        # print path
        return path

    # if two has same distance, head will move to inner most stack
    # TODO fix the same distance issue
    next_head = min(pos_queue_, key=lambda x: abs(x - head_pos_))
    # print 'next head:{}'.format(next_head)
    path.append(next_head)
    new_pos_queue = copy.deepcopy(pos_queue_)
    new_pos_queue.remove(next_head)

    sstf(next_head, new_pos_queue, path)

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
result_path = sstf(head_pos, pos_queue)

print_result(result_path, head_pos)
