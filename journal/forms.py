from django.forms import ModelForm
from .models import Bug, Contact


class BugForm(ModelForm):
    class Meta:
        model = Bug
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BugForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
