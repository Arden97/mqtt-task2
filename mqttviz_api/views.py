import json
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Cryptocurrency

@method_decorator(csrf_exempt, name='dispatch')
class CryptoView(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        sub_data = {
            'id': data.get('id'),
            'rank': data.get('rank'),
            'symbol': data.get('symbol'),
            'name': data.get('name'),
            'supply': data.get('supply'),
            'marketCapUsd': data.get('marketCapUsd'),
            'volumeUsd24Hr': data.get('volumeUsd24Hr'),
            'priceUsd': data.get('priceUsd'),
            'changePercent24Hr': data.get('changePercent24Hr'),
            'vwap24Hr': data.get('vwap24Hr')
        }

        cur = Cryptocurrency.objects.create(**sub_data)
        data = {
            "message": f"{cur.id} added to database"
        }
        return JsonResponse(data, status=201)

    def get(self, request):
        items_data = []
        for obj in Cryptocurrency.objects.all():
            items_data.append({
                'id': obj.id,
                'rank': obj.rank,
                'symbol': obj.symbol,
                'name': obj.name,
                'supply': obj.supply,
                'marketCapUsd': obj.marketCapUsd,
                'volumeUsd24Hr': obj.volumeUsd24Hr,
                'priceUsd': obj.priceUsd,
                'changePercent24Hr':obj.changePercent24Hr,
                'vwap24Hr': obj.vwap24Hr
            })

            data = {
                'items': items_data,
            }

        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class CryptoViewUpdate(View):

    def patch(self, request, item_id):
        data = json.loads(request.body.decode("utf-8"))
        obj = Cryptocurrency.objects.get(id=item_id)
        obj.id = data['id']
        obj.rank = data['rank']
        obj.symbol = data['symbol']
        obj.name = data['name']
        obj.supply = data['supply']
        obj.marketCapUsd = data['marketCapUsd']
        obj.volumeUsd24Hr = data['volumeUsd24Hr']
        obj.priceUsd = data['priceUsd']
        obj.changePercent24Hr = data['changePercent24Hr']
        obj.vwap24Hr = data['vwap24Hr']
        obj.save()

        data = {
            'message': f'{item_id} has been updated'
        }

        return JsonResponse(data)