from django.http import JsonResponse, HttpResponseBadRequest

from django.views.decorators.http import require_http_methods
from app.models import Item, Profile, Character
import json


@require_http_methods(["GET"])
def all_profiles(request):
    try:
        profiles = list(Profile.objects.all().values())
        return JsonResponse(profiles, safe=False)
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Profile not found'}, status=404)


@require_http_methods(["GET"])
def all_inventories(request):
    try:
        inventories = list(Item.objects.all().values())
        return JsonResponse(inventories, safe=False)
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Profile not found'}, status=404)


@require_http_methods(["GET"])
def all_characters(request):
    try:
        characters = list(Character.objects.all().values())
        return JsonResponse(characters, safe=False)
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Profile not found'}, status=404)


@require_http_methods(["GET"])
def profile(request, profile_id):
    try:
        profile = Profile.objects.get(id=profile_id)
        data = {
            'id': profile.id,
            'username': profile.username,
            'hours_played': profile.hours_played,
            'characters_count': profile.characters_count,
            'characters': [{
                'id': character.id,
                'name': character.name,
            } for character in profile.characters.all()]
        }
        return JsonResponse(data, safe=False)
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Profile not found'}, status=404)


@require_http_methods(["GET"])
def inventory(request, character_id):
    try:
        character = Character.objects.get(id=character_id)
        inventory = character.inventory
        data = {
            'id': inventory.id,
            'name': inventory.name,
            'rarity': inventory.rarity,
            'price': inventory.price
        }
        return JsonResponse(data, safe=False)
    except Character.DoesNotExist:
        return JsonResponse({'error': 'Character not found'}, status=404)


@require_http_methods(["GET"])
def character(request):
    search_query = request.GET.get('q', '')
    try:
        character = Character.objects.filter(name__icontains=search_query).values('name', 'class_name', 'lvl', 'inventory')
        return JsonResponse(list(character), safe=False)
    except Character.DoesNotExist:
        return JsonResponse({'error': 'Character not found'}, status=404)


@require_http_methods(["GET", "POST"])
def error(request):
    if request.method == "GET":
        return HttpResponseBadRequest("ERROR")
    else:
        return JsonResponse({'response': "SUCCESS"})


@require_http_methods(["POST"])
def create_item(request):
    try:
        data = json.loads(request.body)
        name = data.get('name')
        rarity = data.get('rarity')
        price = data.get('price')

        item = Item.objects.create(name=name, rarity=rarity, price=price)

        response_data = {
            'id': item.id,
            'name': item.name,
            'rarity': item.rarity,
            'price': item.price
        }
        return JsonResponse(response_data, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
