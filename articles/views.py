from django.shortcuts import render
from rest_framework.views import APIView
from articles import serializers
from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404




class ArticleList(APIView):
    def get(self):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors)

class ArticleDetail(APIView):
    def get(self, article_id):
        articles = get_object_or_404(Article, id=article_id)
        serializers = ArticleSerializer(articles)
        return Response(serializers.data)
    
        