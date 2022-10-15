from django import forms

class CreateMyUser(forms.Form):
    name = forms.CharField(max_length=50)


class UpdateMyUser(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length=50)


class DeleteMyUser(forms.Form):
    id = forms.IntegerField()