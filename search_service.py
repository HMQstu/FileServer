# coding: utf-8
import jieba
import json
import file_service
import simple_file_info


def cal_keys_from_file(file_info):
    file_info_key = __cal_file_info_key(file_info)
    return json.dumps(file_info_key, ensure_ascii=False)


def query_files(role, query):
    query_key = __cal_query_key(query)
    files_list = file_service.visible_files_list(role)
    result = []
    for file_info in files_list:
        key_words_json = file_info.key_words
        key_words = json.loads(key_words_json)
        count = __compare_similar_count(key_words, query_key)

        simple_info = simple_file_info.parse(file_info, role)
        simple_info.sort = count
        if count > 0:
            result.append(simple_info)
    result = sorted(result, key=lambda x: x.sort, reverse=True)
    return result[:3]


def __cut_for_search(src):
    return list(jieba.cut_for_search(src))


def __cal_query_key(query):
    result = []
    result.extend(__cut_for_search(query))
    return result


def __cal_file_info_key(file_info):
    result = []
    file_name = file_info.file_name
    keys = __cut_for_search(file_name)
    result.extend(keys)
    return result


def __compare_similar_count(keys_a, keys_b):
    count = 0
    for a in keys_a:
        for b in keys_b:
            if a == b:
                count += 1
    return count
