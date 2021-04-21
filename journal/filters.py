from .models import Manuscript, Volume, Sections
import django_filters
from django_filters import ModelChoiceFilter
from django import forms


class ManuscriptFilter(django_filters.FilterSet):
    citation_title = django_filters.CharFilter(lookup_expr='icontains', label='Title', widget=forms.TextInput(attrs={
        'placeholder': 'Title contains', 'class': 'form-control p-1'}))

    keywords = django_filters.CharFilter(lookup_expr='icontains', label='Keywords', widget=forms.TextInput(attrs={
        'placeholder': 'Keywords contain', 'class': 'form-control p-1', 'type': 'text'}))

    citation_volume = ModelChoiceFilter(
        queryset=Volume.objects.all(),
        empty_label='Volume',
        label='Volume',
        widget=forms.Select(attrs={
            'placeholder': 'Volume', 'class': 'shadow-sm form-control p-1'}))

    section = ModelChoiceFilter(
        queryset=Sections.objects.all(),
        empty_label='Sections',
        label='Section',
        widget=forms.Select(attrs={
            'class': 'shadow-sm form-control p-1'}))

    abstract = django_filters.CharFilter(lookup_expr='icontains', label='Title', widget=forms.TextInput(attrs={
        'placeholder': 'Abstract contains', 'class': 'form-control p-1'}))

    class Meta:
        model = Manuscript
        fields = ['citation_title', 'keywords', 'citation_volume', ]
