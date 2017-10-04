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


def search(terms, questions):
    res_list = []
    # assume that the key words are separated by the comma,
    # convert from ' barca andrews iniesta' to [barca, andrews, iniesta]
    term_set = set(terms.lower().strip().split(' '))
    print 'term set :{}'.format(term_set)

    for question in questions:
        cur_q = re.sub('[^0-9a-zA-Z ]+', ' ', question['question']).strip()  # clean all non-alphanumeric strings
        cur_q_set = set(cur_q.lower().split(' '))  # set of lowercase words in question

        # if question have all keywords in another list
        if term_set.issubset(cur_q_set):
            temp_dict = question
            temp_dict['answer'] = temp_dict['answers'][0]['text']
            # remove the answers entry from dict
            del temp_dict['answers']

            print temp_dict
            res_list.append(temp_dict)
    print res_list
    print len(res_list)
    # with open('1b.json', 'w') as f:
    #     r = json.dumps(res_list)
    #     f.write(r)


fname = 'qa.json'
raw_json = get_json(fname)
q_json = get_list_questions(raw_json)
search('movie', q_json)
