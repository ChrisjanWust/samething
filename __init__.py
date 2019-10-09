from operator import itemgetter
from .matcher import *


class Thing:

    def __init__(self, search_string):
        self.search_string = search_string


    def same(self, record_string, result_ranking = 1):
        """
        For checking the match confidence of a single record.
        However, samething is more useful when comparing the
        confidence scores of different records matching, as
        opposed to returning a single confidence score in
        isolation.
        :param record_string:
        :param result_ranking:
        :return:
        """
        return match_confidence(self.search_string, record_string, record_ranking= result_ranking)


    def most_same(self, record_string_list, ordered_by_popularity=False):
        """
        If only interesting in the best matching string, this could easily be used like so:
        best_match = list1[thing.most_same(list1)]  # (with thing already declared)
        :param record_string_list: list of possible matching strings
        :param ordered_by_popularity: determines whether the input list has already been ordered by popularity
        :return: index of string the most same string
        """
        result_list_ordered = self.most_same_listed(record_string_list, ordered_by_popularity)
        most_same_index = result_list_ordered[0]['index']
        return most_same_index


    def most_same_listed(self, record_string_list, ordered_by_popularity=False):
        """
        :param record_string_list: List of possible matching strings.
        :param ordered_by_popularity: specifies whether the input list has already been ordered by popularity.
        This could be the situation when searching a site like gsmarena: when searching "S8", it would list
        "Samsung Galaxy S8" before "Blackview S8". If this value is true, the first strings in record_string_list
        is given a small preference in matching confidence.
        :return: List of match dictionaries ordered by confidence scores, descending. Each match dictionary
        contains the index of the match, the string (labelled "name") and the confidence score.
        """
        return_list = []

        for i, record_string in enumerate(record_string_list):
            record_ranking = (i + 1) if ordered_by_popularity else 0
            same = self.same(record_string, record_ranking)
            return_list.append({
                'index': i,
                'name': record_string,
                'confidence': same
            })

        return_list.sort(key=itemgetter('confidence'), reverse=True)
        return return_list


