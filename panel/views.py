from django.shortcuts import render
from django.views import View
# Create your views here.


class PanelMainPageView(View):
    def get(self, request):
        return render(request, 'registration/home.html')
