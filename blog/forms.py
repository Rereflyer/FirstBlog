#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		model = Post					# 哪个模型会被用来创建表单
		fields = ('title', 'text',)		# 哪些字段会在表单里出现