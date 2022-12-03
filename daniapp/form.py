from django.forms import ModelForm
from models import *


class createForum(ModelForm):
    class Meta:
        model = forums
        fields = "__all__"


class discussForm(ModelForm):
    class Meta:
        model = discussions
        fields = "__all__"


