from django.shortcuts import render
from mywatchlist.models import MyWatchlist
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data_barang_mywatchlist = MyWatchlist.objects.all()
    context = {
    'list_barang': data_barang_mywatchlist,
    'nama': 'Vania Azria Wardani',
    'id': '2106650380'
    }

    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")