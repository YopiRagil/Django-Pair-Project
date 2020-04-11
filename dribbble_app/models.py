from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now(), blank=True)
    Bio = models.TextField(blank=True, null=True)

    avatar = models.FileField(upload_to="")


    def __str__(self):
        return self.username + ' : ' + self.email

class UserDesign(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    design = models.FileField(upload_to="")
    title = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateField(default=timezone.now(), blank=True)

    def __str(self):
        return self.username + ' : ' + self.title

class DesignComment(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.ForeignKey(UserDesign,on_delete=models.CASCADE)
    comment = models.TextField(blank=False, null=False)
    username_post = models.CharField(max_length=50)

    def __str(self):
        return self.username + ' - ' + self.title + ', Commented by : ' + self.username_post 

class DesignLike(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.ForeignKey(UserDesign,on_delete=models.CASCADE)
    like = models.IntegerField(default=1)
    username_comment = models.CharField(max_length=50)

    def __str(self):
        return self.username + ' - ' + self.title + ', Liked by : ' + self.username_comment

class CommentLike(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.ForeignKey(UserDesign,on_delete=models.CASCADE)
    comment = models.ForeignKey(DesignComment,on_delete=models.CASCADE)
    like = models.IntegerField(default=1)
    username_like = models.CharField(max_length=50)

    def __str(self):
        return self.username + ' - ' + self.comment + ', Liked by : ' + self.username_like
