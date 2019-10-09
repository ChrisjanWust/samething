from samething.matcher import *
from samething.graphs import Parabola, Polygon
from samething import Thing
from pprint import pprint

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
        'search': 'S8',
        'record': 'Samsung Galaxy S8',
        'rankiing': 0
    },
    {
        'search': 'S8',
        'record': 'Blackview S8',
        'ranking': 7

    },
    {
        'search': 'S8',
        'record': 'Gionee S8',
        'ranking': 6
    }
]


testing_data_2 = [
    {'search': 'Samsung S5', 'record': 'Samsung S5230W Star WiFi'},
    {'search': 'Samsung S5', 'record': 'Samsung S5510'},
    {'search': 'Samsung S5', 'record': 'Samsung S5560 Marvel'},
    {'search': 'Samsung S5', 'record': 'Samsung S5150 Diva folder'},
    {'search': 'Samsung S5', 'record': 'Samsung S5350 Shark'},
    {'search': 'Samsung S5', 'record': 'Samsung S5550 Shark 2'},
    {'search': 'Samsung S5', 'record': 'Samsung S5620 Monte'},
    {'search': 'Samsung S5', 'record': 'Samsung S5250 Wave525'},
    {'search': 'Samsung S5', 'record': 'Samsung S5330 Wave533'},
    {'search': 'Samsung S5', 'record': 'Samsung S5230 Star'},
    {'search': 'Samsung S5', 'record': 'Samsung S5600 Preston'},
    {'search': 'Samsung S5', 'record': 'Samsung S5050'},
    {'search': 'Samsung S5', 'record': 'Samsung S5200'},
    {'search': 'Samsung S5', 'record': 'Samsung S5500 Eco'},
    {'search': 'Samsung S5', 'record': 'Samsung S5630C'},
    {'search': 'Samsung S5', 'record': 'Samsung S5600v Blade'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy Pocket Duos S5302'},
    {'search': 'Samsung S5', 'record': 'Samsung S5780 Wave 578'},
    {'search': 'Samsung S5', 'record': 'Samsung S5233T'},
    {'search': 'Samsung S5', 'record': 'Samsung S5690 Galaxy Xcover'},
    {'search': 'Samsung S5', 'record': 'Samsung S5610'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy Y S5360'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy Y TV S5367'},
    {'search': 'Samsung S5', 'record': 'Samsung Wave Y S5380'},
    {'search': 'Samsung S5', 'record': 'Samsung Rex 80 S5222R'},
    {'search': 'Samsung S5', 'record': 'Samsung Rex 90 S5292'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy Y Plus S5303'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy Star S5280'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy Pocket Neo S5310'},
    {'search': 'Samsung S5', 'record': 'Samsung Star 3 s5220'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy Pop Plus S5570i'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy Pocket S5300'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy Pocket plus S5301'},
    {'search': 'Samsung S5', 'record': 'Samsung S5530'},
    {'search': 'Samsung S5', 'record': 'Samsung S5750 Wave575'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy Gio S5660'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy Mini S5570'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy Ace S5830'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy Ace S5830I'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy Fit S5670'},
    {'search': 'Samsung S5', 'record': 'Samsung S5260 Star II'},
    {'search': 'Samsung S5', 'record': 'Samsung Star 3 Duos S5222'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy S5 Plus'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy S5 Neo'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy Star Trios S5283'},
    {'search': 'Samsung S5', 'record': 'Samsung S5611'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy S5'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy S5 (USA)'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy S5 Duos'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy S5 (octa-core)'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy S5 Active'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy S5 LTE-A G906S'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy S5 Sport'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy S5 mini'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy S5 mini Duos'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy S5 LTE-A G901F'},
    {'search': 'Samsung S5', 'record': 'Samsung Galaxy Tab S5e'}
]


testing_data_listed = [
    'Samsung S5230W Star WiFi',
    'Samsung S5510',
    'Samsung S5560 Marvel',
    'Samsung S5150 Diva folder',
    'Samsung S5350 Shark',
    'Samsung S5550 Shark 2',
    'Samsung S5620 Monte',
    'Samsung S5250 Wave525',
    'Samsung S5330 Wave533',
    'Samsung S5230 Star',
    'Samsung S5600 Preston',
    'Samsung S5050',
    'Samsung S5200',
    'Samsung S5500 Eco',
    'Samsung S5630C',
    'Samsung S5600v Blade',
    'Samsung Galaxy Pocket Duos S5302',
    'Samsung S5780 Wave 578',
    'Samsung S5233T',
    'Samsung S5690 Galaxy Xcover',
    'Samsung S5610',
    'Samsung Galaxy Y S5360',
    'Samsung Galaxy Y TV S5367',
    'Samsung Wave Y S5380',
    'Samsung Rex 80 S5222R',
    'Samsung Rex 90 S5292',
    'Samsung Galaxy Y Plus S5303',
    'Samsung Galaxy Star S5280',
    'Samsung Galaxy Pocket Neo S5310',
    'Samsung Star 3 s5220',
    'Samsung Galaxy Pop Plus S5570i',
    'Samsung Galaxy Pocket S5300',
    'Samsung Galaxy Pocket plus S5301',
    'Samsung S5530',
    'Samsung S5750 Wave575',
    'Samsung Galaxy Gio S5660',
    'Samsung Galaxy Mini S5570',
    'Samsung Galaxy Ace S5830',
    'Samsung Galaxy Ace S5830I',
    'Samsung Galaxy Fit S5670',
    'Samsung S5260 Star II',
    'Samsung Star 3 Duos S5222',
    'Samsung Galaxy S5 Plus',
    'Samsung Galaxy S5 Neo',
    'Samsung Galaxy Star Trios S5283',
    'Samsung S5611',
    'Samsung Galaxy S5',
    'Samsung Galaxy S5 (USA)',
    'Samsung Galaxy S5 Duos',
    'Samsung Galaxy S5 (octa-core)',
    'Samsung Galaxy S5 Active',
    'Samsung Galaxy S5 LTE-A G906S',
    'Samsung Galaxy S5 Sport',
    'Samsung Galaxy S5 mini',
    'Samsung Galaxy S5 mini Duos',
    'Samsung Galaxy S5 LTE-A G901F',
    'Samsung Galaxy Tab S5e'
]



def test_data(data):
    # params
    max_search_string_length = 40
    max_record_string_length = 60
    max_row_length = max_search_string_length + max_record_string_length + 30

    print('-' * max_row_length)
    print('Confidence', '\t',
          'Search String', ' ' * (max_search_string_length - len('Search String')),
          'Record String', ' ' * (max_record_string_length - len('Search String')),
          'Ranking')
    print('-' * max_row_length)
    for pair in data:
        search = pair['search']
        record = pair['record']
        ranking = pair.get('ranking', 0)
        confidence_percentage = round(100 * match_confidence(search, record, record_ranking=ranking), 3)
        print(str(confidence_percentage) + '%   ', '\t',
              search, ' ' * (max_search_string_length - len(search)),
              record, ' ' * (max_record_string_length - len(record)),
              ranking)


def test_data_listed(data):
    thing = Thing('Samsung S5')
    pprint(thing.most_same_listed(data))

# test_data(testing_data_2)


test_data_listed(testing_data_listed)




