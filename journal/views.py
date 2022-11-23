from django.shortcuts import render, get_object_or_404, redirect
from .models import Manuscript, Volume, Author
from django.db.models import Count
from .forms import BugForm, ContactForm
from honeypot.decorators import check_honeypot
from .filters import ManuscriptFilter
from django.core.mail import send_mail


def index(request):
    # This query gives the totals for each degree in a dictionary, then we pass it into the view and loop over it to
    # render the values in Chart.js.
    degree_counts = Author.objects.order_by('degree').values('degree').annotate(Count('id'))

    # These query gives the manuscript totals for each volume.
    m_by_volume_count = Manuscript.objects.order_by('citation_volume').values('citation_volume').annotate(Count('id'))

    # These query gives the manuscript totals for each section.
    section_count = Manuscript.objects.order_by('section__title').values('section__title').annotate(Count('id'))
    manuscript_list = Manuscript.objects.all()
    manuscript_filter = ManuscriptFilter(request.GET, queryset=manuscript_list)

    # Query for all volumes
    volumes = Manuscript.objects.all()
    return render(
        request,
        template_name='index.html',
        context={
            'section_count': section_count,
            "m_by_volume_count": m_by_volume_count,
            "degree_counts": degree_counts,
            "manuscripts": volumes,
            "volumes": Volume.objects.all,
            'filter': manuscript_filter,
        }
    )


def charts(request):
    author_student_count = Author.objects.filter(degree='Student').count()
    author_bsc_count = Author.objects.filter(degree='Bsc').count()
    author_msc_count = Author.objects.filter(degree='Msc').count()
    author_phd_count = Author.objects.filter(degree='PhD').count()
    return render(
        request,
        template_name='statistics.html',
        context={
            "student_count": author_student_count,
            "bsc_count": author_bsc_count,
            "msc_count": author_msc_count,
            "phd_count": author_phd_count,
        }
    )


def advancedsearch(request):
    manuscript_list = Manuscript.objects.all()
    manuscript_filter = ManuscriptFilter(request.GET, queryset=manuscript_list)
    return render(
        request,
        template_name='advanced_search.html',
        context={
            'filter': manuscript_filter,
        }
    )


def abstract(request, slug_field):
    show_abstract = get_object_or_404(Manuscript, slug_field=slug_field)
    return render(request, 'abstract.html', context={
        'abstract': show_abstract,
    }
                  )


def author(request):
    show_author = get_object_or_404(Author, id=id)
    return render(request, template_name='author.html', context={
        'author': show_author,
    })


def volumeview(request, name):
    q = Volume.objects.filter().order_by('last_page')
    show_volume = get_object_or_404(q, name=name)
    show_manuscripts = Manuscript.objects.filter(citation_volume__name__exact=str(name))
    return render(request, 'volumes.html', context={
        'volumes': show_volume,
        'manuscripts': show_manuscripts,

    })


def thanks(request):
    return render(request, template_name='thanks.html')


@check_honeypot(field_name='phonenumber')
def report(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'You have a new bug report'
            from_email = 'dev.jum.mk'
            content = form.cleaned_data['name'] + '\n' + form.cleaned_data['email'] + '\n' + form.cleaned_data['description']
            send_mail(
                subject,
                content,
                from_email,
                ['anovski3@gmail.com', 'dev.jum.mk'],
                fail_silently=False,
            )
            return redirect('thanks')
    else:
        form = BugForm()

    return render(request, template_name='report.html', context={'form': form})


@check_honeypot(field_name='phonenumber')
def contact(request):
    form_class = ContactForm
    contact_form = form_class(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
            subject = 'You have a new bug report'
            from_email = 'dev.jum.mk'
            content = contact_form.cleaned_data['name'] + '\n' + contact_form.cleaned_data['email'] + '\n' + contact_form.cleaned_data['content']
            send_mail(
                subject,
                content,
                from_email,
                ['anovski3@gmail.com', 'dev.jum.mk'],
                fail_silently=False,
            )
            return redirect('thanks')
        else:
            contact_form = ContactForm()

    return render(request, 'contact.html', {'contact_form': contact_form})
