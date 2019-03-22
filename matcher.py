from samething.graphs import Parabola, Polygon
import re

digit_pattern = re.compile('\d') # declared here for performance reasons


def match_confidence(search_string, record_string, record_ranking=0):
    search_words = extract_words(search_string)
    record_words = extract_words(record_string)

    # todo: determine individual scales using machine learning
    confidence = scale_exponentially(nr_words_in_search(search_words), 0.3) \
                 * scale_exponentially(percentage_search_words_matched(search_words, record_words), 1) \
                 * scale_exponentially(percentage_record_words_matched(search_words, record_words), 0.5) \
                 * scale_exponentially(ranking_of_record(record_ranking), 3)

    return normalize_confidence(confidence)


def extract_words(string = ""):
    return remove_empty_strings(string.upper().split(' '))


def normalize_confidence(confidence):
    return scale_exponentially(confidence, 1/3)


def remove_empty_strings(strings):
    return [string for string in strings if len(string) != 0]


def nr_words_in_search(search_words):
    return Parabola(points = [[0, 0], [3, .82], [6, 1]]).y(len(search_words))


def rank_word(word):
    nr_digits = len(digit_pattern.findall(word))
    return Polygon([[0,1], [1,2.2], [4,2.4], [10,2.8]]).y(nr_digits)


def percentage_search_words_matched(search_words, record_words):
    if len(search_words) == 0:
        return 0
    else:
        total_matches = 0
        total_possible = 0
        for word in search_words:
            word_ranked = rank_word(word)
            total_possible += word_ranked
            if word in record_words:
                total_matches += word_ranked

        x = total_matches / total_possible
        return Parabola([[0,0], [.50,.40], [.85,1]]).y(x)


def percentage_record_words_matched(search_words, record_words):
    if len(search_words) == 0:
        return 0
    else:
        total_matches = 0
        total_possible = 0
        for word in record_words:
            word_ranked = rank_word(word)
            total_possible += word_ranked
            if word in search_words:
                total_matches += word_ranked

        x = total_matches / total_possible
        return Parabola([[0,0], [.50,.40], [.85,1]]).y(x)



def nr_search_words_matched(search_words, record_words):
    matches = 0
    for search_word in search_words:
        if search_word in record_words:
            matches += 1

    x = matches
    return Parabola(points = [[0, 0], [3, .82], [8, 1]]).y(x)


def ranking_of_record(record_ranking):
    return Polygon([[1,1], [3,0.9], [20,0.7], [100,0.6]]).y(record_ranking)


def scale_linear(percentage, scale):
    new_percentage = 1 - scale * (1 - percentage)
    if new_percentage < 0:
        new_percentage = 0

    return new_percentage


def scale_exponentially(percentage, scale):
    new_percentage = percentage ** scale
    return new_percentage




# print (Polygon([[0,0], [2,80], [10,100]]).y(6))

# print (scale_exp(1, 0.1))