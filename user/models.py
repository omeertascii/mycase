from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name)
        
        user.set_password(password)
        user.save(using=self._db)
        return user
   
    # Test bilgileri için kendi superuser'ımı oluşturdum. 
    def create_superuser(self, email:str, username:str, first_name:str, last_name:str, password:str):
        user = self.create_user(
            email="omer.tasci@posteffect.ai", 
            username = "admin",
            first_name = "admin",
            last_name = "admin",
            password="admin",
        )
        user.staff = True
        user.superuser = True
        user.save(using=self._db)
        return user
    
    
class User(AbstractBaseUser):
    email = models.EmailField(unique=True, verbose_name="E-Mail")                              
    username = models.CharField(max_length=30, unique=True, verbose_name="Username")     
    first_name = models.CharField(max_length=30, verbose_name="First Name")                   
    last_name = models.CharField(max_length=30, verbose_name="Last Name")       
    staff = models.BooleanField(default=False, verbose_name="Staff")         
    superuser = models.BooleanField(default=False, verbose_name="Super User")    
    active = models.BooleanField(default=True, verbose_name="Activated")     
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Date Join")    
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")  
    deleted = models.BooleanField(default=False, verbose_name="Delete") 
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name','password']    
    
    objects = UserManager()
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.superuser
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_superuser(self):
        return self.superuser
    
    @property
    def is_active(self):
        return self.active
        


    
    def __str__(self):
        return self.username
    


