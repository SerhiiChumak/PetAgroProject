from django.test import TestCase
from agro_catalog.models import Culture, Disease, Drug


class ModelsTests(TestCase):
    def test_culture_str(self):
        culture = Culture.objects.create(name="test")
        self.assertEqual(
            str(culture),
            f"{culture.name}")

    def test_disease_str(self):
        disease = Disease.objects.create(name="test", type="othertest")
        self.assertEqual(
            str(disease),
            f"{disease.name} {disease.type}")

    def test_drug_str(self):
        drug = Drug.objects.create(name="test", price="10", description="testdiscription")
        self.assertEqual(
            str(drug),
            f"{drug.name} {drug.price} {drug.description}")
