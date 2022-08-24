from django.db import models

class Company(models.Model): # 회사 필드

    co_id = models.TextField(primary_key=True) #회사id
    
    def __str__(self):
        return self.co_id

# class Another(models.Model):
#     name = models.CharField(max_length=20)
#     slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

#     def __str__(self) :
#         return self.name

#     def get_absolute_url(self):
#      return f'/recruit/another/{self.slug}'

class Notification(models.Model): # 모델 필드
    company = models.ForeignKey(Company, on_delete = models.CASCADE)#회사id
    no_id = models.TextField() # 채용공고id
    country = models.TextField() # 국가
    region = models.TextField() # 지역
    position = models.TextField() # 포지션
    reward=models.PositiveIntegerField() # 채용보상금
    content=models.TextField() # 채용내용
    technique=models.TextField() #사용기술
    
    def __str__(self):
        return self.company


class User(models.Model): # 유저(지원자) 필드
    user_id = models.TextField(unique=True) # 유저id
    apply_id = models.ForeignKey(Notification,on_delete=models.CASCADE) # 채용공고id





