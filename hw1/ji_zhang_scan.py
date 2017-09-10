def parse_data(fname):
    with open(fname) as f:
        # assume only two lines
        text_list = f.readlines()
        return int(text_list[0]), text_list[1]


def scan(head_pos_, pos_queue_):
    path = []
    left = True
    cur_head_index = 0

    if len(pos_queue_) == 0:
        # print path
        return path
    # if two has same distance, head will move to inner most stack
    # TODO fix the same distance issue
    next_head = min(pos_queue_, key=lambda x: abs(x - head_pos))

    if next_head != head_pos_:
        path.append(next_head)
        cur_head_index = pos_queue_.index(next_head)
        pos_queue_.remove(next_head)

    # print 'next head:{}'.format(next_head)

    # if the head pos is at a same location with a list num
    while head_pos_ == next_head:
        path.append(head_pos_)
        cur_head_index = pos_queue_.index(next_head)
        pos_queue_.remove(head_pos_)

    if 199 not in pos_queue and head_pos < next_head and head_pos != 199:
        pos_queue.append(199)
        left = False

    elif 0 not in pos_queue and head_pos > next_head and head_pos != 0:
        pos_queue.insert(0, 0)
        left = True
        cur_head_index += 1

    # break the list to two parts, first iterate the one
    if left:
        path += list(reversed(pos_queue_[:cur_head_index])) + pos_queue_[cur_head_index:]
    else:
        path += pos_queue_[cur_head_index:] + list(reversed(pos_queue_[:cur_head_index]))

    # print 'path:{}'.format(path)
    return path


# fname = sys.argv[1:][0]

fname = 'test1.txt'
head_pos, raw_pos_queue = parse_data(fname)
# print head_pos, pos_queue

pos_queue = sorted([int(num) for num in raw_pos_queue.split(',')])
# if pos_queue does not has 199, add to it

result_path = scan(head_pos, pos_queue)

tot_cost = abs(head_pos - result_path[0])
for i in range(len(result_path) - 1):
    tot_cost += abs(result_path[i] - result_path[i + 1])

res_path_str = ','.join(str(x) for x in result_path)
print res_path_str, '\n', tot_cost, '\n', '{},{}'.format(result_path[-1], tot_cost)
