import json


def get_json(fname):
    with open(fname) as json_data:
        d = json.load(json_data)
        return d


def get_list_questions(json_raw):
    answer_json_list = []

    for data in json_raw['data']:
        for paras in data['paragraphs']:
            for question in paras['qas']:
                answer_json_list.append(question)
    return answer_json_list


def get_question_stats(question_json):
    categories = ['how', 'how many', 'how much', 'what', 'when',
                  'where', 'which', 'who', 'whom']
    filtered_cate = ['what', 'when', 'where', 'which', 'who', 'whom']
    # init results with categories and 0
    res_dict = {cate: 0 for cate in categories}

    for question in question_json:
        cur_q = question['question'].lower().strip()
        first_word = cur_q.split(' ')[0]
        if first_word == 'how':
            # add to 'how' count
            res_dict[first_word] += 1

            sec_word = cur_q.split(' ')[1]
            if sec_word == 'many' or sec_word == 'much':
                res_dict['{} {}'.format(first_word, sec_word)] += 1

        elif first_word in filtered_cate:
            res_dict[first_word] += 1
    with open('1a.json', 'w') as f:
        r = json.dumps(res_dict)
        f.write(r)

    print res_dict
    return res_dict


fname = 'qa.json'
raw_json = get_json(fname)
q_json = get_list_questions(raw_json)
get_question_stats(q_json)
