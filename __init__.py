from operator import itemgetter
from samething.matcher import *


class Thing:

    def __init__(self, search_string):
        self.search_string = search_string


    def same(self, record_string, result_ranking = None):
        return match_confidence(self.search_string, record_string, record_ranking= result_ranking)


    def most_same(self, record_string_list, ordered_by_popularity=False):
        most_same_index = 0
        most_same = 0

        for i, record_string in enumerate(record_string_list):
            same = self.same(record_string, i)
            if same > most_same:
                most_same = same
                most_same_index = i

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





