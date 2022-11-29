from rest_framework import serializers
from .models import Author, Manuscript, Volume, Sections


class ManuscriptSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True, read_only=True)
    section = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Manuscript
        fields = [
            'id',
            'citation_language',
            'udc',
            'abstract',
            'citation_issn',
            'citation_title',
            'citation_date',
            'citation_volume',
            'keywords',
            'document',
            'authors',
            'section',
        ]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
                  'name',
                  'surname',
                  'institution',
                  ]


class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = [
                  'citation_language',
                  'citation_journal_title',
                  'udc',
                  'citation_issn',
                  'first_page',
                  'last_page',
                  'pdf',
                  'full_date'
                  ]


class SectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = ['title']
4