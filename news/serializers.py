from rest_framework import serializers

from .models import News, NewStatus, Comment, CommentStatus, Status


class NewsSerializer(serializers.ModelSerializer):
    # status_count = serializers.ReadOnlyField(sourse = 'get_status_count')

    class Meta:
        model = News
        fields = "__all__"
        read_only_fields = ['author',]


class CommentSerializer(serializers.ModelSerializer):
    # status_count = serializers.ReadOnlyField(sourse = 'get_status_count')

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['author',]


class StatusSerializer(serializers.ModelSerializer):
    # status_count = serializers.ReadOnlyField(sourse = 'get_status_count')

    class Meta:
        model = Status
        fields = "__all__"
        read_only_fields = ['author',]


class NewsStatusSerializer(serializers.ModelSerializer):
    # status_count = serializers.ReadOnlyField(sourse = 'get_status_count')

    class Meta:
        model = NewStatus
        fields = "__all__"
        read_only_fields = ['author',]


class CommentStatusSerializer(serializers.ModelSerializer):
    # status_count = serializers.ReadOnlyField(sourse = 'get_status_count')

    class Meta:
        model = CommentStatus
        fields = "__all__"
        read_only_fields = ['author',]