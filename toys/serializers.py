from rest_framework import serializers
from toys.models import Toy

class ToySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=250)
    release_date = serializers.DateTimeField()
    toy_category = serializers.CharField(max_length=200)
    was_included_in_home = serializers.BooleanField(required=False)

    def create(self, validate_data):
        return Toy.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.description = validate_data.get('description', instance.description)
        instance.release_date = validate_data.get('release_date', instance.release_date)
        instance.toy_category = validate_data.get('toy_category', instance.toy_category)
        instance.was_included_in_home = validate_data.get('was_included_in_home', instance.was_included_in_home)
        instance.save()
        return instance