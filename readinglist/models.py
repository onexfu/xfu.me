from django.db import models
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Button, HTML
from crispy_forms.bootstrap import FormActions



class ReadingItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(verbose_name="URL")
    note = models.TextField(blank=True, default="")
    is_read = models.BooleanField(default=False)
    read_time = models.DateTimeField(null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % self.name

    @models.permalink
    def to_read_url(self):
        opts = {
            'pk': self.pk
        }
        return ('rlist:to_read', (), opts)

    @models.permalink
    def delete_url(self):
        opts = {
            'pk': self.pk
        }
        return ('rlist:delete', (), opts)


class ReadingItemForm(ModelForm):
    class Meta:
        model = ReadingItem
        exclude = ('read_time')

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        HTML('<legend>{% if is_create%}Create{%else%}Edit{%endif%} reading item</legend>'),
        Field('name', css_class='input-xlarge'),
        Field('url', css_class='input-xxlarge'),
        Field('note', rows="10", css_class='input-xxlarge'),
        Field('is_read'),
        FormActions(
            Submit('save', 'Save'),
            HTML('<a href="{% url rlist:unread-list %}" class="btn">Cancel</a>')
        )
    )
     
