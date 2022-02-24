from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class OwnUserManager(BaseUserManager):

    def create_user(self, login, password=None):

        if not login:
            return ValueError('User must have login.')

        user = self.model(login=login)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, login, password=None):

        user = self.create_user(login=login, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


def definePathToStorePhoto(instance, filename):

    if hasattr(instance, 'login'):
        return '{0}/namePhoto'.format(instance.login)
    else:
        return 'tempFilesForPhoto'

class OwnUser(AbstractBaseUser, PermissionsMixin):

    userId = models.AutoField(primary_key=True)
    login = models.CharField(max_length=255, unique=True) #нужно ли данное поле?
    # name = models.CharField(max_length=255)
    # surname = models.CharField(max_length=255) #нужно ли данное поле?
    phone = models.CharField(max_length=20)
    # email = models.EmailField(max_length=255, unique=True) #нужно ли данное поле?
    rating = models.FloatField(null=True, blank=True, default=None)
    userImage = models.ImageField(upload_to=definePathToStorePhoto)
    hasUserActivePoint = models.BooleanField(default=False)
    userCity = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    objects = OwnUserManager()

    # def getFullName(self):
        # return '{0} {1}'.format(self.surname, self.name)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"