from .models import Manuscript, Volume, Sections
import django_filters
from django_filters import ModelChoiceFilter
from django import forms


class ManuscriptFilter(django_filters.FilterSet):
    citation_title = django_filters.CharFilter(lookup_expr='icontains', label='Title', widget=forms.TextInput(attrs={
        'placeholder': 'Title contains', 'class': 'form-control p-1 shadow-sm w-100 my-2 mx-2',
        'style': 'border-radius:6px; font-weight:300;'}))

    keywords = django_filters.CharFilter(lookup_expr='icontains', label='Keywords', widget=forms.TextInput(attrs={
        'placeholder': 'Keywords contain', 'class': 'shadow-sm form-control p-1 w-100 my-2 mx-2', 'type': 'text',
        'style': 'border-radius:6px; font-weight:300;'}))

    citation_volume = ModelChoiceFilter(
        queryset=Volume.objects.all(),
        empty_label='Select Volume',
        label='Volume',
        widget=forms.Select(attrs={
            'placeholder': 'Volume', 'class': 'shadow-sm form-control p-1 shadow-sm w-100 my-2 mx-2',
            'style': 'border-radius:6px; font-weight:300;'}))

    section = ModelChoiceFilter(
        queryset=Sections.objects.all(),
        empty_label='Select Section',
        label='Section',
        widget=forms.Select(attrs={
            'class': 'shadow-sm form-control p-1 shadow-sm w-100 my-2 mx-2', 'style': 'border-radius:6px; font-weight:300;'}))

    abstract = django_filters.CharFilter(lookup_expr='icontains', label='Title', widget=forms.TextInput(attrs={
        'placeholder': 'Abstract contains', 'class': 'form-control p-1 shadow-sm w-100 my-2 mx-2 ',
        'style': 'border-radius:6px; font-weight:300;'}))

    class Meta:
        model = Manuscript
        fields = ['citation_title', 'keywords', 'citation_volume', 'abstract', 'section']
