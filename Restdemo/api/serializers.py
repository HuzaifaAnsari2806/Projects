from rest_framework import serializers

from .models import BlogPost


class BolgPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogPost
        fields=['id','title','content','published_date']