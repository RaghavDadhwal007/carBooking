from django.db import models


class UserRole(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=225, unique=True, null=True)

    def __str__(self):
        return self.role


class RoleDetails(models.Model):
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="", null=True)
    email = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255, default="", null=True)
    mobile = models.CharField(max_length=255, default="", null=True)
    address = models.CharField(max_length=255, default="", null=True)
    gender = models.CharField(max_length=255, default="", null=True)
    otp = models.CharField(max_length=255, default="", null=True)
    otp_time = models.CharField(max_length=255, default="", null=True)
    verify_link = models.CharField(max_length=255, default="", null=True)
    login_time = models.CharField(max_length=255, default="", null=True)
    active = models.NullBooleanField(default=0)


class LoginDetails(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(primary_key=True, max_length=255)
    login = models.CharField(max_length=255, default="", null=True)
    logout =  models.CharField(max_length=255, default="", null=True)
    address = models.CharField(max_length=255, default="", null=True)
