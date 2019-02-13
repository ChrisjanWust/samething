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




