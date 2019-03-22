from samething.graphs import Parabola, Polygon
import re

digit_pattern = re.compile('\d')  # declared here for performance reasons. (Odd way to check for digits, I know)


#                       MAIN FUNCTION
def match_confidence(search_string, record_string, record_ranking=0):
    search_words = extract_words(search_string)
    record_words = extract_words(record_string)

    # todo: determine individual scales using machine learning
    confidence = scale_exponentially(nr_words_in_search(search_words), 0.3) \
                 * scale_exponentially(percentage_search_words_matched(search_words, record_words), 1) \
                 * scale_exponentially(percentage_record_words_matched(search_words, record_words), 0.5) \
                 * scale_exponentially(ranking_of_record(record_ranking), 3)

    return scale_exponentially(confidence, 1/3)  # confidence is normalized.



#                         METRICS FUNCTIONS

# Each of these methods returns a confidence score (out of 1).
# These scores are then combined to produce the final confidence score.


def nr_words_in_search(search_words):
    return Parabola(points = [[0, 0], [3, .82], [6, 1]]).y(len(search_words))


def percentage_search_words_matched(search_words, record_words):
    x = percentage_words_matched(search_words, record_words)
    return Parabola([[0,0], [.50,.40], [.85,1]]).y(x)


def percentage_record_words_matched(search_words, record_words):
    x = percentage_words_matched(record_words, search_words)
    return Parabola([[0, 0], [.50, .40], [.85, 1]]).y(x)


def ranking_of_record(record_ranking):
    return Polygon([[1,1], [3,0.9], [20,0.7], [100,0.6]]).y(record_ranking)



#                   HELPER FUNCTIONS

def extract_words(string = ""):
    return remove_empty_strings(string.upper().split(' '))


# if the words fully match, return 1.
# If they partially match, return lower scores.
# And obviously, if they don't match at all, return 0
def matches_word(word1, word2):
    if word1 == word2:
        return 1
    if word1 in word2:
        if word1.startswith(word2):
            return 0.7
        else:
            return 0.5
    if word2 in word1:
        if word1.startswith(word2):
            return 0.6
        else:
            return 0.45
    return 0


# uses matches_word on a list of matches
def best_word_match(lookup_word, possible_match_words):
    match_scores = [matches_word(lookup_word, possible_match_word) for possible_match_word in possible_match_words]
    best_match_score = max(match_scores)
    return best_match_score


def remove_empty_strings(strings):
    return [string for string in strings if len(string) != 0]


# searches for occurences of lookup_words in possible_match_words
# keep count of the total_matches and total_possible matches
# finally express as a percentage by dividing
def percentage_words_matched(lookup_words, possible_match_words):
    if len(possible_match_words) == 0:
        return 0
    else:
        total_matches = 0
        total_possible = 0
        for word in lookup_words:
            word_ranked = rank_word(word)
            total_possible += word_ranked
            if word in possible_match_words:
                total_matches += word_ranked

        percentage = total_matches / total_possible
        return percentage


# words with digits are more important than words without.
# (matching 'S8' is more important than matching 'Galaxy')
# The more digits in a word, the higher the probability of
# it being a model number
def rank_word(word):
    nr_digits = len(digit_pattern.findall(word))
    return Polygon([[0,1], [1,2.2], [4,2.4], [10,2.8]]).y(nr_digits)


def scale_linear(percentage, scale):
    new_percentage = 1 - scale * (1 - percentage)
    if new_percentage < 0:
        new_percentage = 0

    return new_percentage


def scale_exponentially(percentage, scale):
    return percentage ** scale
