from rest_framework import serializers
from django.db.models import Sum 

from .models import Blog,BlogImages,Statistics

class BlogImagesSerializer(serializers.ModelSerializer):
    images=serializers.ImageField(use_url=False)
    class Meta:
        model = BlogImages
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    images = BlogImagesSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True  # This field should not be included in the serialized output
    )

    class Meta:
        model = Blog
        fields = ['title', 'content', 'uploaded_images', 'images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])

        # Create the Blog instance
        blog = Blog.objects.create(**validated_data)

        # Create BlogImages instances associated with the Blog
        for image in uploaded_images:
            BlogImages.objects.create(blog=blog, images=image)

        return blog

class StatSerializer(serializers.ModelSerializer):
    total_sum=serializers.IntegerField(read_only=True)
    class Meta:
        model=Statistics
        fields=['field_name','value','total_sum']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        total_sum = Statistics.objects.aggregate(total_sum=Sum('value'))['total_sum']
        representation['total_sum'] = total_sum
        return representation
