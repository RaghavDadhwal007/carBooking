from django import forms
from front_panel.models import RoleDetails


class RoleDetailsForm(forms.ModelForm):
    class Meta:
        model = RoleDetails
        exclude = ["role", "name", "email", "password", "mobile", "address", "gender",
                   "otp", "otp_time", "verify_link", "login_time", "active"]