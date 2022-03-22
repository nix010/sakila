from django.urls import path
from rest_framework.routers import DefaultRouter

from sakila.views import FilmViewSet, CategoryViewSet, CustomerListView, CustomerViewSet, ActorListView, ActorViewSet

router = DefaultRouter()

router.register(r'films', FilmViewSet, basename='films')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'actor', ActorViewSet, basename='actor')

urlpatterns = [
    path('customer/', CustomerListView.as_view()),
    path('actor/', ActorListView.as_view()),
]

