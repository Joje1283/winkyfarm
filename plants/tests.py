from django.test import TestCase
from .models import Plant


class TestPlant(TestCase):
    def setUp(self) -> None:
        pass

    def test_create_model(self):
        plant = Plant.objects.create(name="지키라", species="파키라")
        self.assertEqual(plant.name, "지키라")
        self.assertEqual(plant.species, "파키라")
        self.assertEqual(plant.period, 7)
        self.assertIsNone(plant.last_water_date)
