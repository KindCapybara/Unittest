geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def search_visit_ru():
    visit_all = []
    for visit_rus in geo_logs:
        for visits, [Sity, Country] in visit_rus.items():
            if Country == 'Россия':
                visit_all.append(visit_rus)
    return visit_all


def search_uniq_id():
    geo_id = ids.values()
    uniq_id = set()
    for value in geo_id:
        for id in value:
            uniq_id.add(id)
    return list(uniq_id)


def max_sales_amount():
    max_stat = max(stats, key=stats.get)
    amount = max_stat, stats[max_stat]
    return amount
