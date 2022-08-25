from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class User(AbstractUser):

    # 手机号
    moblie=models.CharField(max_length=11,unique=True,blank=False)
    # 头像
    avatar=models.ImageField(upload_to='avatar/%Y%m%d/',blank=True)
    # 简介
    user_desc=models.CharField(max_length=500,blank=True)
    class Meta:
        # 修改表名
        db_table='tb_users'
        # admin后台显示
        verbose_name='用户管理'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.moblie








