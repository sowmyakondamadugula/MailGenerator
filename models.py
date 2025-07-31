from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class UserLogin(models.Model):
    user_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Increased length for hashed passwords

    def set_password(self, raw_password):
        """Hash and store the password"""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Verify hashed password"""
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.email