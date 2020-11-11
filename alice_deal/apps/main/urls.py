from django.urls import path

from . import views

app_name = 'main'

urlpatterns = (
    [
        path('', views.index, name='index'), # homepage
        path('introduction/', views.intro, name='intro'), # introduction
        path('historical_context/', views.background, name='background'), # historical context
        path('miss_alice_deal/', views.alice_deal, name='alice_deal'), # miss alice deal
        path('in_memoriam/', views.memoriam, name='memoriam'), # in memoriam
        path('alice_deal_junior_high/', views.school, name='school'), # alice deal junior high        
        path('research/', views.research, name='research'), # research
        path('document/<slug:doc_id>/', views.document, name='document'),
    ]
)
