from django.db import models
from django.urls import reverse


class Sections(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Volume(models.Model):
    citation_language = 'en'
    citation_issn = '1409-9055'
    udc = '57 91'
    citation_journal_title = 'Bulletin of the biology students\' research society'
    name = models.CharField(max_length=30)
    issn = 'ISSN: 1409 - 9055'
    pdf = models.FileField(upload_to='volumes/pdfs/%Y')
    first_page = models.CharField(max_length=10, db_index=True)
    last_page = models.CharField(max_length=10, db_index=True)
    date = models.IntegerField(verbose_name='Година на издавање', db_index=True)
    full_date = models.DateField(verbose_name='Целосен датум на издавање')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('volume_view', kwargs={
            'name': self.name
        })


class Author(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    surname = models.CharField(max_length=100, db_index=True)
    degree = models.CharField(max_length=10, default='Student', db_index=True)
    email = models.EmailField(max_length=80, default="", blank=True, null=True, db_index=True)
    institution = models.CharField(max_length=255, verbose_name='Институција + Адреса', db_index=True)
    image = models.ImageField(upload_to='img/', max_length=100, null=True, blank=True, db_index=True)

    def __str__(self):
        return '%s %s' % (self.name, self.surname)

    class Meta:
        ordering = ['institution']

    def get_absolute_url(self):
        return reverse('author', kwargs={
            'id': self.id
        })


class Manuscript(models.Model):
    # These are specific to this journal
    citation_language = 'en'
    citation_issn = '1409-9055'
    udc = '57 91'
    citation_journal_title = 'Bulletin of the biology students\' research society'

    # These are all important
    citation_title = models.CharField(max_length=255, verbose_name='Наслов на трудот', db_index=True)
    title = models.TextField(verbose_name='Декориран наслов', db_index=True)
    citation_date = models.DateField(verbose_name='Датум на публикување', db_index=True)
    citation_volume = models.ForeignKey(Volume, on_delete=models.CASCADE, verbose_name='Том', db_index=True)
    citation_firstpage = models.CharField(max_length=10, verbose_name='Број на првата страница', db_index=True)
    citation_lastpage = models.CharField(max_length=10, verbose_name='Број на последната страница', db_index=True)
    authors = models.ManyToManyField(Author, verbose_name='Автор/и', db_index=True)
    reference_author = models.EmailField(max_length=60, verbose_name='E-mail на првиот автор', db_index=True)
    abstract = models.TextField(verbose_name='Извод', db_index=True)
    keywords = models.CharField(max_length=300, verbose_name='Клучни зборови', db_index=True)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE, default=1, verbose_name='Секција', db_index=True)
    # PDF
    document = models.FileField(upload_to='pdfs/', verbose_name='.pdf', db_index=True)
    slug_field = models.SlugField(max_length=50, verbose_name='Скратено', unique=True, db_index=True)

    class Meta:
        ordering = ['citation_volume']

    def __str__(self):
        return '%s %s' % (
            str(self.citation_volume) + ' -- ' + str(self.citation_date), self.citation_title)

    def get_absolute_url(self):
        return reverse('abstract-detail', kwargs={
            'slug_field': self.slug_field
        })


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False, null=False, db_index=True)

    def __str__(self):
        return self.title


class PostTag(models.Model):
    tag_name = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    content = models.TextField(blank=False, null=False, db_index=True)
    image = models.ImageField(upload_to='post_images', blank=False, db_index=True)
    tag = models.ManyToManyField(PostTag)
    slug = models.SlugField(max_length=50, unique=True, blank=True, db_index=True)

    def __str__(self):
        return self.title


class Bug(models.Model):
    name = models.CharField(max_length=50, verbose_name='First and last name')
    email = models.EmailField(max_length=70, verbose_name='Your e-mail')
    description = models.TextField(verbose_name='Describe the issue in detail')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    content = models.TextField()

    def __str__(self):
        return self.name
