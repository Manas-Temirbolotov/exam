import kwargs as kwargs
import slug as slug
from django.shortcuts import render
from requests import Response
from rest_framework import generics, authentication, permissions, request
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter

import news
from .models import News, NewStatus, Comment, CommentStatus, Status
from .serializers import NewsSerializer, CommentSerializer, CommentStatusSerializer, StatusSerializer, \
    NewsStatusSerializer
from .mixins import NewsStatusMixin, CommentStatusMixin, StatusMixin

from .permissions import ReadOnlyPermission, IsAuthorPermission


class NewsListCreateAPIView(generics.ListCreateAPIView, NewsStatusMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [ReadOnlyPermission, ]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    search_fields = ['title', ]
    filterset_fields = ['created', ]
    ordering_fields = ['created', ]

    def get_queryset(self):
        super().get_queryset().filter(news_id=self.kwargs.get('news_id'))

    def perform_create(self, serializer):
        serializer.save(
            news_id = self.kwargs.get('news_id'),
            author = self.request.user
        )


class NewsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView, NewsStatusMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [IsAuthorPermission, ]

    def get_queryset(self):
        super().get_queryset().filter(news_id=self.kwargs.get('news_id'))


class CommentListCreateAPIView(generics.ListCreateAPIView,CommentStatusMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [ReadOnlyPermission, ]

    def get_queryset(self):
        super().get_queryset().filter(comment_id=self.kwargs.get('comment_id'))

    def perform_create(self, serializer):
        serializer.save(
            comment_id=self.kwargs.get('comment_id'),
            author=self.request.user
        )


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView, CommentStatusMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [IsAuthorPermission, ]

    def get_queryset(self):
        super().get_queryset().filter(comment_id=self.kwargs.get('comment_id'))


class StatusListCreateAPIView(generics.ListCreateAPIView, StatusMixin):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [IsAuthorPermission, ]

    def get_queryset(self):
        super().get_queryset().filter(status_id=self.kwargs.get('status_id'))

    def perform_create(self, serializer):
        serializer.save(
            status_id=self.kwargs.get('status_id'),
            author=self.request.user
        )

@action(methods = ['POST'], detail=True, permissions_classes = [permissions.IsAuthenticated])
def status(self, request, pk = None):
    status = self.get_object()
    author = request.user
    new_status = Status(
        slug=slug,
        author=author,
        status=status,
    )
    new_status.save()
    data = {
        "massage": f'Status успешно выставлен id = {news.id} пользователем id {request.user.id}'
    }
    return Response(data, status=200)


class StatusRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView, StatusMixin):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [IsAuthorPermission, ]

    def get_queryset(self):
        super().get_queryset().filter(status_id=self.kwargs.get('status_id'))


class NewsStatusRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView, NewsStatusMixin):
    queryset = Status.objects.all()
    serializer_class = NewsStatusSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [IsAuthorPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(
            news_status_id=self.kwargs.get('news_status_id'))

    def post(self, request, *args, **kwargs):
        news_id = kwargs.get('news_id')
        author = request.user
        status = kwargs.get('status')
        new_status = Status(
            news_id=news_id,
            author=author,
            status=status
        )
        new_status.save()
        return Response(status=200)


class CommentStatusRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView,CommentStatusMixin):
    queryset = CommentStatus.objects.all()
    serializer_class = CommentStatusSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [IsAuthorPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(
            comment_status_id=self.kwargs.get('comment_status_id'))

    def post(self, request, *args, **kwargs):
        comment_id = kwargs.get('comment_id')
        author = request.user
        status = kwargs.get('status')
        new_status = Status(
            news_id=comment_id,
            author=author,
            status=status
        )
        new_status.save()
        return Response(status=200)