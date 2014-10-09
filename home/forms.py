from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import Field

from .models import Post


class CompletePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompletePostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'create_post'
        self.helper.form_class = 'form-control'
        self.helper.form_method = 'post'


        self.helper.layout = Layout(
            Field("post_body")
        )

    class Meta:
        model = Post

class SelfPostForm(forms.Form):
    """
    Prints a form to self post
    """
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = "create_new_post"
        self.helper.form_class = "form-inline"
        self.helper.form_method = "post"
        self.helper.form_action = "/home/post/new/"
        self.helper.form_show_labels = False

    post_body = forms.CharField(
        label="",
        max_length=100,
        required=True,
    )
