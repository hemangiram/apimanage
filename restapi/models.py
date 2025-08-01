from django.db import models



class Nurse(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    doctor = models.ManyToManyField(Nurse, related_name='patients')

    def __str__(self):
        return self.name


class Doctor(models.Model):
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctor_records')
    today_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')  # media/uploads/ में सेव होगा

    def __str__(self):
        return self.title
    

class FileUpload(models.Model):
    file = models.FileField(upload_to='upload/')


    def __str__(self):
        return self.file.name
    