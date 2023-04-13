# user/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):  # UserModel에서 AbstractUser(장고기본유저모델)를 사용하겠다
    class Meta:
        db_table = "my_user"  # 여기는 테이블 이름이에요! 꼭 기억 해 주세요!

    # 기본 모델에 없던 것만 추가 (닉네임, 프로필이미지)
    nickname = models.CharField(max_length=15, default='')
    user_img = models.FileField("이미지", upload_to='',blank=True, null=True)
