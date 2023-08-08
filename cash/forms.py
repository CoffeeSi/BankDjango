from django import forms



class Transfer_money(forms.Form):
    cd = forms.CharField(label='' ,widget=forms.TextInput(
        attrs={'class':'input-card', 'placeholder':'Номер счёта'}))
    mn = forms.IntegerField(label='' ,widget=forms.TextInput(
        attrs={'class':'input-money', 'placeholder':'Сумма'}))