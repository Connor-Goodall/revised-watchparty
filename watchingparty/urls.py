from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView


app_name = 'watchingparty'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},
    name='logout'),
    path('profile/', views.profileDetail, name='profile'),
    path('edit/', views.settingsDetail, name='settings'),
    path('edit/save/', views.profileSettings, name='save'),
    path('planMovie/', views.planMovie, name='planMovie'),
     path('<movietitle>/<description>/', views.movieInfo, name='movieInfo'),
    path('delete/<movietitle>/<description>/', views.deleteEvent, name='deleteEvent'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('results/', views.SearchResultsView.as_view(), name='searchResults'),

]
