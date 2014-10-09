from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import Field

from .models import Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'create_post'
        self.helper.form_class = 'form-control'
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Field("post_body")
        )

    class Meta:
        model = Post