from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models

# Create your models here.



class UserManager(BaseUserManager):


    def create_user(self, email , password=None , **kwargs ):
        
        if not email:
            raise ValueError("users must have en email assigned ") 
        user_obj = self.model(email=self.normalize_email(email),  **kwargs)
        user_obj.set_password(password)
        user_obj.save(using= self._db)
        return user_obj
    

    def create_superuser(self , email , password):
        super_user = self.create_user( email , password)
        super_user.is_staff = True
        super_user.is_superuser = True
        super_user.save(using= self._db)
        return super_user


     

class User(AbstractBaseUser , PermissionsMixin):
    """Custom user that support email insted of Username """

    email     = models.EmailField(unique=True)
    name      = models.CharField( max_length=255)
    is_active = models.BooleanField( default=True)
    is_staff = models.BooleanField( default=False)

    objects = UserManager()

    USERNAME_FIELD= 'email'

