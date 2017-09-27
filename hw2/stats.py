import json

import re


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
        cur_q = question['question'].lower()
        first_word = cur_q.split(' ')[0]
        if first_word == 'how':
            sec_word = cur_q.split(' ')[1]
            if sec_word == 'many' or sec_word == 'much':
                res_dict['{} {}'.format(first_word, sec_word)] += 1
            else:
                res_dict[first_word] += 1
        elif first_word in filtered_cate:
            res_dict[first_word] += 1

    with open('1a_stats.json', 'w') as f:
        r = json.dumps(res_dict)
        f.write(r)

    print res_dict
    return res_dict


def search(terms, questions):
    res_list = []
    # assume that the key words are separated by the comma,
    # convert from 'barca, andrews iniesta' to [barca, andrews, iniesta]
    term_set = set(' '.join(terms.lower().split(',')).split(' '))
    print 'term set :{}'.format(term_set)
    for question in questions:
        cur_q = re.sub('[^0-9a-zA-Z ]+', '', question['question'])  # clean all non-alphanumeric strings
        cur_q_set = set(cur_q.lower().split(' '))  # set of lowercase words in question

        # print cur_q
        # print cur_q_set

        if not term_set.isdisjoint(cur_q_set):  # if two set share words
            temp_dict = question
            temp_dict['answer'] = temp_dict['answers'][0]['text']
            # remove the answers entry from dict
            del temp_dict['answers']

            res_list.append(temp_dict)

    with open('1b_search_res.json', 'w') as f:
        r = json.dumps(res_list)
        f.write(r)


fname = 'qa.json'
raw_json = get_json(fname)
q_json = get_list_questions(raw_json)
get_question_stats(q_json)
search('determined', q_json)
