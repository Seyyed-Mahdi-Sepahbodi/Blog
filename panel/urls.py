from django.urls import path
from .views import PanelMainPageView

urlpatterns = [
    path('', PanelMainPageView.as_view(), name='panel_main_page'),
]
