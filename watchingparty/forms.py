from django import forms

from watchingparty import models


class ProfileForms(forms.Form):
    class Meta:
        model = models.Profile;