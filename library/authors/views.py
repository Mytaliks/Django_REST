from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .models import Article
from rest_framework.response import Response
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework import viewsets
from rest_framework.decorators import action
from .filters import ArticleFilter


class ArticleAPIVIew(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def article_view(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


class ArticleCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]

    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

class ArticleViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]

    @action(detail=True, methods=['get'])
    def article_text_only(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        return Response({'article.text': article.text})

    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def article_text_only(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        return Response({'article.text': article.text})


class ArticleKwargsFilterView(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Article.objects.filter(name__contains=name)


class ArticleParamFilterViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        articles = Article.objects.all()
        if name:
            articles = articles.filter(name__contains=name)
        return articles

class ArticleDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['name', 'user']

class ArticleCustomDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_class = ArticleFilter