from django.db import models
from user.models import UserModel

# 게시글 테이블 모델
class Post(models.Model):
    class Meta:
        db_table = "posting"
        
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post_author = models.CharField("작성자", max_length=256) # user 모델의 사용자를 상속받습니다. 추후에 바뀌어야 합니다.
    post_title = models.CharField("글제목", max_length=45)
    post_content = models.TextField("글내용")
    post_img = models.FileField("이미지", upload_to='',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
