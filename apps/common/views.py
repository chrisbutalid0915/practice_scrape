from django.shortcuts import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the common index.")
