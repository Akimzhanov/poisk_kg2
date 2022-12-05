from rest_framework import serializers
from PIL import Image, ImageFilter
from .models import Post
from .utils import normalize_phone




class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('storage', 'title','image', 'blur_image', 'status','reward', 'text', 'category', 'address', 'date', 'whatsapp', 'telegram' )

        # <PIL.Image.Image image mode=RGB size=225x225 at 0x7FDAF19C76D0>


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
        a = validated_data['image']
        img = Image.open(a)
        global blur
        blur = img.filter(ImageFilter.GaussianBlur(6))
        blur.show()
        validated_data['blur_image'] = str(blur)
        # blur.save()
        post = super().create(validated_data)
        post.save()
        return post
    
    def save(self, **kwargs):
        return super().save(**kwargs)
