from django.db import models

# Create your models here.


class Fcuser(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    class Meta:
        db_table = 'ssk_user'
        verbose_name = '사용잦'
        verbose_name_plural = '사용자'
