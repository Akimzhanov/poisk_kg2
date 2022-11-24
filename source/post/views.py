from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.generics import ListAPIView
from .models import Post
from .serializers import  PostListSerializer,PostCreateSerializer
from django_filters import rest_framework as rest_filter






class PostViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [filters.SearchFilter,
    rest_filter.DjangoFilterBackend,
    filters.OrderingFilter]
    search_fields = ['title']
    filterset_fields = ['category']
    ordering_fields = ['created_at']


    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action == 'create':
            return PostCreateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()




# class FindViewSet(ListAPIView):
#     queryset = Storage.objects.filter(storage='find')
#     serializer_class = StorageListSerializer


# class LostViewSet(ListAPIView):
#     queryset = Storage.objects.filter(storage='lost')
#     serializer_class = StorageListSerializer



