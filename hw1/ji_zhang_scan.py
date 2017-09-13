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


def scan(head_pos_, pos_queue_):
    path = []
    left = True
    cur_head_index = 0

    zero_added = False
    end_added = False

    if len(pos_queue_) == 0:
        # print path
        return path, []
    # if two has same distance, head will move to inner most stack
    next_head = get_closest_num(head_pos_, pos_queue_)

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

    if 199 not in pos_queue_ and head_pos_ < next_head and head_pos_ != 199:
        pos_queue_.append(199)
        left = False
        end_added = True



    elif 0 not in pos_queue_ and head_pos_ > next_head and head_pos_ != 0:
        pos_queue_.insert(0, 0)
        left = True
        cur_head_index += 1  # this is needed as it inserted in the beginning of the list
        zero_added = True

    # break the list to two parts, first iterate the one
    if left:
        path += list(reversed(pos_queue_[:cur_head_index])) + pos_queue_[cur_head_index:]
    else:
        path += pos_queue_[cur_head_index:] + list(reversed(pos_queue_[:cur_head_index]))

    print path
    added_index_list = []
    if zero_added:
        added_index_list.append(path.index(0))
    if end_added:
        added_index_list.append(path.index(199))

    # print 'path:{}'.format(path)
    return path, added_index_list


# fname = 'test1.txt'
if sys.argv[1:]:
    fname = sys.argv[1:][0]
    # fname = 'test1.txt'

    head_pos, raw_pos_queue = parse_data(fname)
    # print head_pos, pos_queue

    pos_queue = sorted([int(num) for num in raw_pos_queue.split(',')])
    origin_queue = pos_queue[:]

    result_path, add_index_list = scan(head_pos, pos_queue)

    tot_cost = abs(head_pos - result_path[0])
    for i in range(len(result_path) - 1):
        tot_cost += abs(result_path[i] - result_path[i + 1])

    # print 'added list:{}'.format(add_index_list)
    # clean added 199 and 0
    for index in enumerate(result_path):
        index = int(index[0])
        if index in add_index_list:
            del result_path[index]

    res_path_str = ','.join(str(x) for x in result_path)
    print res_path_str, '\n', tot_cost, '\n', '{},{}'.format(result_path[-1], tot_cost)
