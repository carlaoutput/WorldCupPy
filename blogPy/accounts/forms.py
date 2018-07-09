
# Form for sign-in up on the Soccer Blog created by CarlaPastor

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):  # OJO we dont want to name this the same
    class Meta:
        fields = ("username", "email", "password1", "password2") #tuple
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"  # labels for the actual field
        self.fields["email"].label = "Email address"