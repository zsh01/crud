from tkinter.tix import Form
from traceback import format_stack

from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields = "__all__"