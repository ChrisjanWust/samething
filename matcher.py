from samething.graphs import Parabola, Polygon
import re


digit_pattern = re.compile('\d') # declared here for performance reasons


def match_confidence(search_string, record_string):
    search_words = extract_words(search_string)
    record_words = extract_words(record_string)

    # todo: determine individual scales using machine learning
    confidence = scale_exponentially(nr_words_in_search(search_words), 0.3) \
                 * scale_exponentially(percentage_search_words_matched(search_words, record_words), 1) \
                 * scale_exponentially(percentage_record_words_matched(search_words, record_words), 0.5)

    return normalize_confidence(confidence)


def extract_words(string = ""):
    return remove_empty_strings(string.upper().split(' '))


def normalize_confidence(confidence):
    return scale_exponentially(confidence, 1/3)


def remove_empty_strings(strings):
    return [string for string in strings if len(string) != 0]


def nr_words_in_search(search_words):
    x = len(search_words)
    y = Parabola(points = [[0, 0], [3, .82], [6, 1]]).y(x)
    return y


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
    y = Parabola(points = [[0, 0], [3, .82], [8, 1]]).y(x)
    return y


def scale_linear(percentage, scale):
    new_percentage = 1 - scale * (1 - percentage)
    if new_percentage < 0:
        new_percentage = 0

    return new_percentage


def scale_exponentially(percentage, scale):
    new_percentage = percentage ** scale
    return new_percentage


def test_data(data):
    # params
    max_search_string_length = 45
    max_row_length = 120

    print('-' * max_row_length)
    print('Confidence', '\t', 'Search String', ' ' * (max_search_string_length - len('Search String')), 'Record String')
    print('-' * max_row_length)
    for pair in data:
        search = pair['search']
        record = pair['record']
        confidence_percentage = round(100 * match_confidence(search, record), 3)
        print (str(confidence_percentage) + '%   ', '\t', search, ' ' * (max_search_string_length - len(search)), record)


testing_data = [
    {
        'search': 'Apple iPhone 8 128GB',
        'record': 'Apple iPhone 8 4.7", 64 GB, Fully Unlocked, Gold'
    },
    {
        'search': 'Samsung S9 64GB Black',
        'record': 'Samsung Galaxy S8 64GB Black'
    },
    {
        'search': 'Samsung S9 64GB Black',
        'record': 'Samsung S9 64GB'
    },
    {
        'search': 'Samsung Galaxy S9 64GB Black',
        'record': 'Samsung Galaxy S8 64GB Black'
    },
    {
        'search': 'Samsung Galaxy S9 64GB Black',
        'record': 'Samsung S9 64GB'
    },
    {
        'search': 'iPhone 8 128GB',
        'record': 'IPhone 8 128Gb'
    },
    {
        'search': 'APPLE iPhone 8 128GB',
        'record': 'Apple Iphone 8 128Gb'
    },
    {
        'search': '',
        'record': ''
    }
]

# print (Polygon([[0,0], [2,80], [10,100]]).y(6))

# print (scale_exp(1, 0.1))