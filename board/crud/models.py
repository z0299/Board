from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    """
    1. models.py에서 모델 변경사항을 적용한다
    2. python manage.py makemigrations 명령어를 실행하여
       변경사항에 대한 migration을 만든다
    3. python manage.py migrate 명령어를 실행하여
       변경사항을 데이터베이스에 적용한다
    """
