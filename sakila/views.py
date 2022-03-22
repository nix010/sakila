from django.views.generic import ListView

from sakila.models import Film, Category, Customer, Actor
from sakila.serializers import FilmSerializer, CategorySerializer, CustomerSerializer, ActorSerializer
from rest_framework import viewsets, mixins


class FilmViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,

    viewsets.GenericViewSet
):
    serializer_class = FilmSerializer
    queryset = Film.objects


class CategoryViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,

    viewsets.GenericViewSet
):
    serializer_class = CategorySerializer
    queryset = Category.objects


class CustomerViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,

    viewsets.GenericViewSet
):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.order_by('-created_at')


class ActorViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,

    viewsets.GenericViewSet
):
    serializer_class = ActorSerializer
    queryset = Actor.objects.order_by('-created_at')


class CustomerListView(ListView, ):

    queryset = Customer.objects.order_by('-created_at')
    template_name = 'customer/list.html'


class ActorListView(ListView, ):

    queryset = Actor.objects.order_by('-created_at')
    template_name = 'actor/list.html'
