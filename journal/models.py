from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


class Sections(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Issue(models.Model):
    name = models.CharField(max_length=120)
    number = models.IntegerField(blank=False)
    date_created = models.DateTimeField()

    def __str__(self):
        return str(self.number) + '  ' + str(self.date_created)


class Volume(models.Model):
    name = models.CharField(max_length=30, default='Your volume name')
    citation_language = models.CharField(max_length=20, unique=False)
    citation_issn = models.CharField(max_length=20)
    udc = models.CharField(blank=True, max_length=10)
    citation_journal_title = models.CharField(blank=True, max_length=120)
    pdf = models.FileField(blank=True, upload_to='volumes/pdfs/%Y')
    first_page = models.CharField(max_length=10, db_index=True)
    last_page = models.CharField(max_length=10, db_index=True)
    date = models.IntegerField(verbose_name='Publishing year')
    full_date = models.DateField(verbose_name='Full date')
    issue = models.ManyToManyField(Issue)

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
    institution = models.CharField(max_length=255, verbose_name='Institution and address', db_index=True)
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
    image = models.ImageField(blank=True, upload_to='manuscript_images/')
    citation_language = models.CharField(max_length=10)
    citation_issn = models.CharField(max_length=16)
    udc = models.CharField(max_length=8)
    # These are all important
    citation_title = models.CharField(max_length=255, verbose_name='Manuscript title')
    title = HTMLField(verbose_name='Decorated title')
    citation_date = models.DateField(verbose_name='Publishing date')
    citation_volume = models.ForeignKey(Volume, on_delete=models.CASCADE, verbose_name='Volume', db_index=True)
    citation_firstpage = models.CharField(max_length=10, verbose_name='First page number')
    citation_lastpage = models.CharField(max_length=10, verbose_name='Last page number')
    authors = models.ManyToManyField(Author, verbose_name='Author/s', db_index=True)
    reference_author = models.EmailField(max_length=60, verbose_name='Reference author')
    abstract = HTMLField(verbose_name='Abstract')
    keywords = models.CharField(max_length=300, verbose_name='Key words')
    section = models.ForeignKey(Sections, on_delete=models.CASCADE, default=1, verbose_name='Section')
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


class Journal(models.Model):
    issn = models.CharField(max_length=12)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post)


class ManuscriptReview(models.Model):
    email = models.EmailField(max_length=255, verbose_name='email')
    phone = models.CharField(max_length=255, verbose_name='phone')
    main_author = models.CharField(max_length=255, verbose_name='main_author')
    title = models.CharField(max_length=255, verbose_name='Manuscript title')
    file = models.FileField(upload_to='review/manuscripts/')
    keywords = models.CharField(max_length=255, verbose_name='keywords')
    author_full_address = models.CharField(max_length=255, verbose_name='author_full_address')

    def __str__(self):
        return self.main_author
