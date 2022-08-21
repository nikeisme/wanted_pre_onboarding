from django.db import models

class Company(models.Model): # 회사 필드
    co_id = models.TextField(primary_key=True)
    
    def __str__(self):
        return self.co_id

class Notification(models.Model):
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    no_id = models.TextField()
    country = models.TextField()
    region = models.TextField()
    position = models.TextField()
    reward=models.PositiveIntegerField()
    content=models.TextField()
    technique=models.TextField()

    def __str__(self):
        return self.company


class User(models.Model):
    user_id = models.TextField(unique=True)
    apply_id = models.ForeignKey(Notification,on_delete=models.CASCADE)





