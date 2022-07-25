from django.db import models


class WaterLog(models.Model):
    plant = models.ForeignKey(to="Plant", on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="물 준 시간", auto_now_add=True)


class Plant(models.Model):
    name = models.CharField(verbose_name="이름", max_length=50)
    species = models.CharField(verbose_name="종", max_length=50, default="")
    period = models.IntegerField(verbose_name="물주기 기간", default=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def last_water_date(self):
        return self.waterlog_set.order_by("-created_at").first()

    def give_water(self):
        WaterLog.objects.create(plant=self)