from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import StrictButton, Field, FormActions


class ExampleForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'form-control'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))

    like_website = forms.TypedChoiceField(
        label="Do you like this website?",
        choices=((1, "Yes"), (0, "No")),
        coerce=lambda x: bool(int(x)),
        widget=forms.RadioSelect,
        initial='1',
        required=True,
    )

    favorite_food = forms.CharField(
        label="What is your favorite food?",
        max_length=80,
        required=True,
    )

    favorite_number = forms.IntegerField(
        label="Favorite number",
        required=False,
    )

    notes = forms.CharField(
        label="Additional notes or feedback",
        required=False,
    )


class LoginForm(forms.Form):
    email = forms.CharField(
        label="Email",
        max_length=80,
        required=True,
        )

    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password",
    )
    remember_me = forms.BooleanField()

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_method = 'post'
        self.helper.form_action = '/login/'

        self.helper.form_class = 'form-horizontal'

        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'

        self.helper.layout = Layout(
           Field("email"),
           Field("password"),
           Field("remember_me"),

           FormActions(
               Submit('log_in', 'Log In', css_class=" btn-primary btn-block"),
           )
        )