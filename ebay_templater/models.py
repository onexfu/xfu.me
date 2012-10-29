import markdown

from django.db import models
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Button, HTML
from crispy_forms.bootstrap import FormActions



class Template(models.Model):
    title = models.CharField(max_length=100)
    des = models.TextField(verbose_name="Description")
    des_html = models.TextField()
    album_name = models.CharField(max_length=100, verbose_name="Picasa album name")
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % self.title
    
    def save(self, *args, **kwargs):
        self.des_html = markdown.markdown(self.des)
        super(Template, self).save(*args, **kwargs)

    @models.permalink
    def edit_url(self):
        opts = {
            'pk': self.pk
        }
        return ('templater:edit', (), opts)

    @models.permalink
    def view_url(self):
        opts = {
            'pk': self.pk
        }
        return ('templater:view', (), opts)

    @models.permalink
    def delete_url(self):
        opts = {
            'pk': self.pk
        }
        return ('templater:delete', (), opts)


class TemplateForm(ModelForm):
    class Meta:
        model = Template
        exclude = ('des_html',)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        HTML('<legend>{% if is_create %}Create{%else%}Edit{%endif%} Template</legend>'),
        Field('title', css_class='input-xxlarge'),
        Field('des', rows="10", css_class='input-xxlarge'),
        Field('album_name', css_class='input-xlarge'),
        FormActions(
            Submit('save', 'Save'),
            HTML('<a href="{% url templater:index %}" class="btn">Cancel</a>')
        )
    )














        
