from samething.matcher import *


class Thing:

    def __init__(self, search_string):
        self.search_string = search_string


    def same(self, record_string):
        return match_confidence(self.search_string, record_string)


    def most_same(self, record_string_list):
        most_same_index = 0
        most_same = 0

        for i in range(len(record_string_list)):
            same = self.same(record_string_list[i])
            if same > most_same:
                most_same = same
                most_same_index = i

        return most_same_index




