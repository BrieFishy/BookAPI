from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category="fantasy")
    serializer_class = BookSerializer


class ChildrensViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category="children's")
    serializer_class = BookSerializer


class NonfictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category="nonfiction")
    serializer_class = BookSerializer


class HistoricalViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category="historical")
    serializer_class = BookSerializer


class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category="romance")
    serializer_class = BookSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category="comedy")
    serializer_class = BookSerializer


class AdventureViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category="adventure")
    serializer_class = BookSerializer


class ScienceFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category="science fiction")
    serializer_class = BookSerializer


class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category="mystery")
    serializer_class = BookSerializer


class PoetryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category="poetry")
    serializer_class = BookSerializer

