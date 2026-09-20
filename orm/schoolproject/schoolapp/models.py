from django.db import models

# Create your models here.
class College(models.Model):
    college_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    motto = models.TextField()
    city = models.CharField(max_length=255)

    class Meta:
        db_table = 'college'

    def __str__(self):
        return f"\nid: {self.college_id}\nname: {self.name}\nmotto: {self.motto}\ncity: {self.city}\n"

class Principal(models.Model):
    principal_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True)
    qualification = models.CharField(max_length=255)
    
    college = models.OneToOneField(College, on_delete=models.CASCADE)

    class Meta:
        db_table = 'principal'

    def __str__(self):
        return f"\n{self.principal_id}\n{self.name}\n{self.email}\n{self.qualification}\n{self.college_id}\n"

class Subject(models.Model):
    subject_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = 'subjects'

    def __str__(self):
        return f"\n{self.subject_code}\n{self.name}\n{self.description}\n"

class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    subject_code = models.ManyToManyField(Subject)
    
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return f"\n{self.teacher_id}\n{self.name}\n{self.email}\n{self.qualification}\n{self.subject_code}\n"