import sys

import ji_zhang_scan  # is this fine???


def parse_data(fname):
    with open(fname) as f:
        # assume only two lines
        text_list = f.readlines()
        return int(text_list[0]), text_list[1]


def f_scan(head_pos_, pos_queue_):
    path = []
    extra = 0

    while len(pos_queue_) > 10:
        first_list = sorted(pos_queue_[:10])
        # copy list of rest positions, in case 199 and 0 added to mess up the index
        cur_path, cur_extra = ji_zhang_scan.scan(head_pos_, first_list)
        extra += cur_extra
        path += cur_path

        # update head position and position list
        head_pos_ = path[-1]
        pos_queue_ = pos_queue_[10:]

    if len(pos_queue_) <= 10:
        pos_queue_ = sorted(pos_queue_)
        cur_path, cur_extra = ji_zhang_scan.scan(head_pos_, pos_queue_)
        extra += cur_extra
        path += cur_path

    return path, extra


# fname = sys.argv[1:][0]
if sys.argv[1:]:
    fname = sys.argv[1:][0]
    # fname = 'test5.txt'

    head_pos, raw_pos_queue = parse_data(fname)
    print 'head:{}'.format(head_pos)
    # not same with scan or sstf, not sorted list
    pos_queue = ([int(num) for num in raw_pos_queue.split(',')])
    result_path, extra = f_scan(head_pos, pos_queue)

    tot_cost = abs(head_pos - result_path[0]) + extra
    for i in range(len(result_path) - 1):
        tot_cost += abs(result_path[i] - result_path[i + 1])

    res_path_str = ','.join(str(x) for x in result_path)
    print res_path_str, '\n', tot_cost, '\n', '{},{}'.format(result_path[-1], tot_cost)
