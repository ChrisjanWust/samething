from .graphs import Parabola, Polygon
import re

digit_pattern = re.compile('\d')  # declared here for performance reasons. (Odd way to check for digits, I know)


#                       MAIN FUNCTION

def match_confidence(search_string, record_string, record_ranking=0):
    search_words = _extract_words(search_string)
    record_words = _extract_words(record_string)

    confidence = scale_exponentially(_nr_words_in_search(search_words), 0.3) \
                 * scale_exponentially(_percentage_search_words_matched(search_words, record_words), 1) \
                 * scale_exponentially(_percentage_record_words_matched(search_words, record_words), 0.5) \
                 * scale_exponentially(_ranking_of_record(record_ranking), 3)

    return scale_exponentially(confidence, 1/3)  # confidence is normalized.


def best_word_match(lookup_word, possible_match_words):
    match_scores = [matches_word(lookup_word, possible_match_word) for possible_match_word in possible_match_words]
    best_match_score = max(match_scores)
    return best_match_score


#                         METRICS FUNCTIONS

# Each of these methods returns a confidence score (out of 1).
# These scores are then combined to produce the final confidence score.


def _nr_words_in_search(search_words):
    return Parabola(points=[[0, 0], [3, .82], [6, 1]]).y(len(search_words))


def _percentage_search_words_matched(search_words, record_words):
    x = _percentage_words_matched(search_words, record_words)
    return Parabola([[0,0], [.50,.40], [.85,1]]).y(x)


def _percentage_record_words_matched(search_words, record_words):
    x = _percentage_words_matched(record_words, search_words)
    return Parabola([[0, 0], [.50, .40], [.85, 1]]).y(x)


def _ranking_of_record(record_ranking):
    return Polygon([[1,1], [3,0.9], [20,0.7], [100,0.6]]).y(record_ranking)



#                   HELPER FUNCTIONS

def _extract_words(string=""):
    return _remove_empty_strings(string.upper().split(' '))


def matches_word(lookup_word, possible_match_word):
    """
    :param lookup_word: string
    :param possible_match_word: string
    :return: matching score, from 0-1. If the words
    fully match, return 1. If they partially match,
    return lower scores. And obviously, if they
    don't match at all, return 0
    """
    if lookup_word == possible_match_word:
        return 1
    if lookup_word in possible_match_word:
        if lookup_word.startswith(possible_match_word):
            return 0.7
        else:
            return 0.5
    if possible_match_word in lookup_word:
        if lookup_word.startswith(possible_match_word):
            return 0.6
        else:
            return 0.45
    return 0


def _remove_empty_strings(strings):
    return [string for string in strings if len(string) != 0]


def _percentage_words_matched(lookup_words, possible_match_words):
    """
    searches for occurences of lookup_words in possible_match_words
    keep count of the total_matches and total_possible matches
    finally express as a percentage by dividing
    :param lookup_words: list of strings
    :param possible_match_words: list of strings
    :return: percentage, from 0-1
    """
    if len(possible_match_words) == 0:
        return 0
    else:
        total_matches = 0
        total_possible = 0
        for word in lookup_words:
            word_ranked = _rank_word(word)
            total_possible += word_ranked
            best_match = best_word_match(word, possible_match_words)  # a score (between 0 and 1) is returned
            total_matches += best_match * word_ranked  # because the score is 0, the

        percentage = total_matches / total_possible
        return percentage


def _rank_word(word):
    """
    words with digits are more important than words without.
    (matching 'S8' is more important than matching 'Galaxy')
    The more digits in a word, the higher the probability of
    it being a model number
    :param word: str
    :return: word importance. A regular word would be scored as 1,
    and this would increase based on the number of digits. Max is
    2.8 for 10 digits in the word.
    """
    nr_digits = len(digit_pattern.findall(word))
    return Polygon([[0,1], [1,2.2], [4,2.4], [10,2.8]]).y(nr_digits)


def scale_linear(percentage, scale):
    new_percentage = 1 - scale * (1 - percentage)
    if new_percentage < 0:
        new_percentage = 0

    return new_percentage


def scale_exponentially(percentage, scale):
    return percentage ** scale



