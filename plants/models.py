from django.db import models


class Plant(models.Model):
    name = models.CharField(verbose_name="이름", max_length=50)
    species = models.CharField(verbose_name="종", max_length=50, default="")
    period = models.IntegerField(verbose_name="물주기 기간", default=7)
    last_water_date = models.DateTimeField(verbose_name="마지막으로 물 준 시간", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
