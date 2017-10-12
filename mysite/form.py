#coding:utf8
form django import forms

class ContactForm(forms.Form):
    CITY = [
        ['TP','Taipei'],
        ['TY','Taoyuang'],
        ['TC','Taichung'],
        ['TN','Tainan'],
        ['KS','Kaohsiung'],
        ['NA','Others'],
    ]
    user_name = forms.CharField(label='您的名字',max_length=50,initial='李达')
    user_city = forms.ChoiceField(label='居住城市',choices=CITY)
    user_school = forms.BooleanField(label='是否在学',required=False)
    user_email = forms.EmailField(label='电子邮件')
    user_message = forms.CharField(label='您的意见',widget=forms.Textarea)