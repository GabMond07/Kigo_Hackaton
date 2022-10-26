from dataclasses import fields
from tkinter import Widget
from xml.dom.minidom import Attr
from django import forms
from .models import Report

# We make a form for user information


class Report_form(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        exclude = ['id_code']