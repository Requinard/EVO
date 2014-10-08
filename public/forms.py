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

        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'

        self.helper.layout = Layout(
            Field("email"),
            Field("password"),
            Field("remember_me"),

            FormActions(
                Submit('log_in', 'Log In', css_class=" btn-primary btn-block"),
            )
        )


class RegisterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        helper = FormHelper()

        helper.form_method = 'post'
        helper.form_action = '/register/'

        helper.form_class = "form-horizontal"

        helper.label_class = 'col-sm-3'
        helper.field_class = 'col-sm-8'

        helper.layout = Layout(
            Field("first_name"),
            Field("last_name"),
            Field("email"),
            Field("password"),
            Field("password_repeat"),

            Submit("submit", "Submit", css_class="btn-primary btn-block")
        )

        self.helper = helper

    first_name = forms.CharField(
        label="What's your first name?",
        max_length=30,
        required=True,
    )

    last_name = forms.CharField(
        label="What's your last name?",
        max_length=30,
        required=True
    )

    password = forms.CharField(
        label="Password",
        max_length=30,
        widget=forms.PasswordInput,
        required=True
    )
    password_repeat = forms.CharField(
        label="Password (Repeat it)",
        max_length=30,
        widget=forms.PasswordInput,
        required=True
    )

    email = forms.CharField(
        max_length=30,
        required=True,
    )