from django.db import models
from django.conf import settings
from django.contrib.auth.models import(BaseUserManager, AbstractBaseUser)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, firstName, lastName, password=None):
        if not email or not firstName or not lastName:
            raise ValueError('bosh qator mavjdu')
        if password in None or len(password) < 6:
            raise ValueError('password kiritilmadi yokida yetarli emas!')

        user = self.model(
            email=self.normalize_email(email),
            firstName=firstName,
            lastName=lastName,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, firstName, lastName, password=None):
        if not email or not firstName or not lastName:
            raise ValueError('bosh qator mavjdu')
        if password in None or len(password) < 6:
            raise ValueError('password kiritilmadi yokida yetarli emas!')

        user = self.model(
            email,
            firstName=firstName,
            lastName=lastName,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, blank=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName']

    def __str__(self):
        return "{}- {}".format(self.firstName, self.lastName)
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin