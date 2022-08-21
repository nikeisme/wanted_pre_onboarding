from django import forms
from recruit.models import Notification

# 채용공고 지원폼
class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification  # 사용할 모델
        fields = ['company', 
                  'no_id',
                  'country',
                  'region',
                  'position',
                  'reward',
                  'content',
                  'technique',]  # QuestionForm에서 사용할 Question 모델의 속성