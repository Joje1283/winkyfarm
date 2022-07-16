from django.test import TestCase
from .models import Plant, WaterLog


class TestPlant(TestCase):
    def setUp(self) -> None:
        self.plant = Plant.objects.create(name="지키라", species="파키라")

    def test_model_data(self):
        """
        plant 테이블에 생성된 데이터를 확인
        """
        self.assertEqual(self.plant.name, "지키라")
        self.assertEqual(self.plant.species, "파키라")
        self.assertEqual(self.plant.period, 7)
        self.assertIsNone(self.plant.last_water_date)

    def test_give_water(self):
        """
        물 준 기록이 잘 생성되었는지 확인
        """
        self.assertEqual(WaterLog.objects.count(), 0)
        self.plant.give_water()
        self.assertEqual(WaterLog.objects.count(), 1)
        water_log = self.plant.last_water_date
        self.assertEqual(water_log.plant, self.plant)

