from rest_framework import serializers

from sakila.models import Film, Category, Customer, Actor


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = ('id', 'title', 'language_id', 'release_year')

    title = serializers.CharField()
    language_id = serializers.IntegerField()
    release_year = serializers.IntegerField(min_value=1000, max_value=3000)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', )

    name = serializers.CharField()


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id', 'name', 'age')

    name = serializers.CharField()


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name')

    name = serializers.CharField()
