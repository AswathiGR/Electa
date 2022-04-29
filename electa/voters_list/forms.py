from django import forms  
from voters_list.models import Voters_list  
class VotersForm(forms.ModelForm):  
    class Meta:  
        model = Voters_list  
        fields = "__all__"  