# -*- coding:utf-8 -*-
import re 
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=30)
    email = forms.EmailField(label='邮箱')
    password1 = forms.CharField(
                                label='密码',
                                widget=forms.PasswordInput()
                                )
    password2 = forms.CharField(
                                label='密码(确认)',
                                widget=forms.PasswordInput()
                                )

    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('亲,请输入相同密码.')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError(
                                        '用户名不匹配')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('用户名可能已经存在.')