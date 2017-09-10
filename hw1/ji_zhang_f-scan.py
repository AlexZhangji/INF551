import ji_zhang_scan  # is this fine???


def parse_data(fname):
    with open(fname) as f:
        # assume only two lines
        text_list = f.readlines()
        return int(text_list[0]), text_list[1]


def f_scan(head_pos_, pos_queue_):
    path = []

    while len(pos_queue_) > 10:
        first_list = sorted(pos_queue_[:11])
        # copy list of rest posistions, in case 199 and 0 added to mess up the index
        rest_list = pos_queue_[11:]
        path += ji_zhang_scan.scan(head_pos_, first_list)

        # update head position and position list
        head_pos_ = path[-1]
        pos_queue_ = rest_list

    if len(pos_queue_) <= 10:
        pos_queue_ = sorted(pos_queue_)
        path += ji_zhang_scan.scan(head_pos_, pos_queue_)

    return path


def print_result(res_path, head_pos_):
    tot_cost = abs(head_pos_ - res_path[0])
    for i in range(len(res_path) - 1):
        tot_cost += abs(res_path[i] - res_path[i + 1])

    res_path_str = ','.join(str(x) for x in res_path)
    print res_path_str, '\n', tot_cost, '\n', '{},{}'.format(res_path[-1], tot_cost)


# fname = sys.argv[1:][0]

fname = 'test7.txt'
head_pos, raw_pos_queue = parse_data(fname)
print 'head:{}'.format(head_pos)
# not same with scan or sstf, not sorted list
pos_queue = ([int(num) for num in raw_pos_queue.split(',')])
result_path = f_scan(head_pos, pos_queue)
print_result(result_path, head_pos)
