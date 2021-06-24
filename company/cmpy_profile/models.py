from django.db import models

class Webdev(models.Model):
    webdev_id= models.AutoField
    web_name= models.CharField(max_length=50)
    web_description= models.CharField(max_length=200)
    image= models.ImageField(upload_to="webdevelopment/images", default="")

    def __str__(self):
        return self.web_name


class Mobdev(models.Model):
    mobdev_id = models.AutoField
    mob_name = models.CharField(max_length=50)
    mob_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="mobiledevelopment/images", default="")

    def __str__(self):
        return self.mob_name

class Cloud(models.Model):
    cloud_id = models.AutoField
    cloud_name= models.CharField(max_length=50)
    cloud_description=models.CharField(max_length=200)
    image = models.ImageField(upload_to= "cloud/images",default="")

    def __str__(self):
        return self.cloud_name

class UI_UX(models.Model):
    ui_id=models.AutoField
    ui_name=models.CharField(max_length=50)
    ui_description=models.CharField(max_length=200)
    image =models.ImageField(upload_to="Ui/images",default="")

    def __str__(self):
        return self.ui_name

class Video_editing(models.Model):
    video_id=models.AutoField
    video_name=models.CharField(max_length=50)
    video_description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="video/images", default="")

    def __str__(self):
        return self.video_name


class CMS(models.Model):
    cms_id = models.AutoField
    cms_name = models.CharField(max_length=50)
    cms_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="cms/images", default="")

    def __str__(self):
        return self.cms_name


class HDR(models.Model):
    hdr_id = models.AutoField
    hdr_name = models.CharField(max_length=50)
    hdr_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="hdr/images", default="")

    def __str__(self):
        return self.hdr_name

class Contact(models.Model):
    cont_name= models.CharField(max_length=50)
    cont_email=models.EmailField()
    cont_desc= models.CharField(max_length=450, default="")
    cont_file=models.FileField()
    def __str__(self):
        return self.cont_name



# Create your models here.
