from django.urls import path

from . import views

app_name = 'main'

urlpatterns = (
    [
        path('', views.index, name='index'),
        path('background/', views.background, name='background'),
        path('alice_deal/', views.alice_deal, name='alice_deal'),
        path('school/', views.school, name='school'),
        path('document/<slug:doc_id>/', views.document, name='document'),
    ]
)
