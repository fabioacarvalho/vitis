from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, Row, Column
from django.urls import reverse

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu 
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        #In the case of Django forms, calling super().__init__(*args, **kwargs) initializes the form with any data 
        #that might have been passed during instantiation. This is a common pattern in Python when you override a method in a subclass and want to invoke the same method in the parent class.
        
        #adding date widget to specific forms :
        # self.fields['effective_date'].widget = forms.DateInput(attrs={'type': 'date'})
        # self.fields['warranty_expiration'].widget = forms.DateInput(attrs={'type': 'date'})
        #
        
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('father', css_class='col-md-4'),
                Column('name', css_class='col-md-4'),
                Column('active', css_class='col-md-4'),
            ),
            Row(
                Column('url', css_class='col-md-4'),
                Column('admin', css_class='col-md-4'),
                Column('support', css_class='col-md-4'),
            ),
            Row(
                Column('icon', css_class='col-md-4'),
                Column('order', css_class='col-md-4'),
            ),
        )

        self.helper.form_id = 'id-menuForm'
        # self.helper.form_method = 'post'
        # self.helper.form_action = 'changeform-edit'
        # self.helper.disable_csrf = True
        # self.helper.add_input(Submit('submit', 'Save'))