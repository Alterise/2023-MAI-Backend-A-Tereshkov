import random

from django.http import JsonResponse

from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def profile(request):
    user_profile = {
        'username': random.choice(['reathwer', 'oginthes', 'erntimpy', 'asoleash', 'rablogli']) +
                    str(random.randint(1, 1000)),
        'hours_played': random.randint(1, 10000),
        'characters_count': random.randint(1, 10)
    }
    return JsonResponse(user_profile)


@require_http_methods(["GET", "POST"])
def inventory(request, character_id):
    random.seed(character_id)
    items = [
        {
            'name': random.choice(['Sword', 'Bow', 'Staff']) + " of " +
                    random.choice(['Devilry', 'Jinx', 'Abjuration', 'Sorcery', 'Charm']),
            'rarity': random.choice(['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary']),
            'price': random.randint(1, 50000)
        } for _ in range(random.randint(1, 5))
    ]
    return JsonResponse(items, safe=False)


@require_http_methods(["GET", "POST"])
def character(request, character_id):
    random.seed(character_id)
    character_info = {
        'id': character_id,
        'name': random.choice(['Arukalis', 'Aharith', 'Anvedel', 'Elassaem', 'Ophetrixi']) + " The " +
                random.choice(['Powerful', 'Evil', 'Ancient', 'Devious', 'Divine']),
        'class': random.choice(['Warrior', 'Archer', 'Mage']),
        'lvl': random.randint(1, 80)
    }
    return JsonResponse(character_info)
