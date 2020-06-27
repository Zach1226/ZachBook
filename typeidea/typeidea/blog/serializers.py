from rest_framework import serializers, pagination

from .models import Post, Category, Tag


class PostSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    tag = serializers.SlugRelatedField(many=True,
                                       read_only=True,
                                       slug_field='name')
    owner = serializers.SlugRelatedField(read_only=True, slug_field='username')
    created_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Post
        fields = [
            'url', 'id', 'desc', 'title', 'category', 'tag', 'owner',
            'created_time'
        ]
        extra_kwargs = {'url': {'view_name': 'api-post-detail'}}


class PostDetailSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'category', 'tag', 'owner', 'content_html',
            'created_time'
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'url',
            'id',
            'name',
            'created_time',
        )
        extra_kwargs = {'url': {'view_name': 'api-category-detail'}}


class CategoryDetailSerializer(CategorySerializer):
    posts = serializers.SerializerMethodField('paginated_category')

    def paginated_category(self, obj):
        posts = obj.post_set.filter(status=Post.STATUS_NORMAL)
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(posts, self.context['request'])
        serializer = PostSerializer(
            page, many=True, context={'request': self.context['request']})
        return {
            'count': posts.count(),
            'results': serializer.data,
            'previous': paginator.get_previous_link(),
            'next': paginator.get_next_link(),
        }

    class Meta:
        model = Category
        fields = ('id', 'name', 'created_time', 'posts')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'url',
            'id',
            'name',
            'created_time',
        )
        extra_kwargs = {'url': {'view_name': 'api-tag-detail'}}


class TagDetailSerializer(TagSerializer):
    posts = serializers.SerializerMethodField('paginated_tag')

    def paginated_tag(self, obj):
        posts = obj.post_set.filter(status=Post.STATUS_NORMAL)
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(posts, self.context['request'])
        serializer = PostSerializer(
            page, many=True, context={'request': self.context['request']})
        return {
            'count': posts.count(),
            'results': serializer.data,
            'previous': paginator.get_previous_link(),
            'next': paginator.get_next_link(),
        }

    class Meta:
        model = Tag
        fields = ('id', 'name', 'created_time', 'posts')
