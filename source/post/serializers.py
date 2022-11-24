from rest_framework import serializers
from PIL import Image, ImageFilter
from .models import Post
from .utils import normalize_phone

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('storage', 'title', 'blur_image', 'status', 'text', 'category', 'address', 'date', 'whatsapp', 'telegram' )
        

class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        exclude = ['slug', 'status', 'blur_image']
        
    def validate_whatsapp(self, whatsapp):
        whatsapp = normalize_phone(whatsapp)
        if len(whatsapp) != 13:
            raise serializers.ValidationError('Не верный формат телефона')
        return whatsapp 
        
    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        # post.create_slug()
        return post
