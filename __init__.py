from operator import itemgetter
from samething.matcher import *


class Thing:

    def __init__(self, search_string):
        self.search_string = search_string

    # for checking the match confidence of a single record.
    # However, samething is more useful when comparing the
    # confidence of different records matching, which is what
    # the other two methods do
    def same(self, record_string, result_ranking = None):
        return match_confidence(self.search_string, record_string, record_ranking= result_ranking)


    # if only interesting in the best match, this could easily be used like so:
    # best_match = list1[thing.most_same(list1)]  # (with thing already declared)
    def most_same(self, record_string_list, ordered_by_popularity=False):
        result_list_ordered = self.most_same_listed(record_string_list, ordered_by_popularity)
        most_same_index = result_list_ordered[0]['index']
        return most_same_index


    def most_same_listed(self, record_string_list, ordered_by_popularity=False):
        return_list = []

        for i, record_string in enumerate(record_string_list):
            same = self.same(record_string, i)
            return_list.append({
                'index': i,
                'name': record_string,
                'confidence': same
            })

        return_list.sort(key=itemgetter('confidence'), reverse=True)

        return return_list


