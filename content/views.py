from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')  # select * from content_feed;, 게시글 최신 순으로 가져오기

        return render(request, "instagram_django/main.html", context=dict(feeds=feed_list))