from django import forms

class AisatsuForm(forms.Form):

    list1 = [
        ('1','大変不満'),
        ('2','不満'),
        ('3','どちらでもない'),
        ('4','満足'),
        ('5','大変満足'),
    ]

    date = forms.DateField(label="date")
    name = forms.CharField(label="name",min_length = 3)
    area = forms.CharField(label="area")
    age = forms.IntegerField(label="age")
    mail = forms.EmailField(label="mail")
    url = forms.URLField(label="url")
    check = forms.NullBooleanField(label="check")
    choice = forms.ChoiceField(label="感想",choices = list1,widget=forms.SelectMultiple(attrs={'size':5}))

class IdKensaku(forms.Form):
    id = forms.IntegerField(label = "ID")
