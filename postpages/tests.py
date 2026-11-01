from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

from .models import Postpage


class PostpageValidationTests(SimpleTestCase):
    def make_post(self, **overrides):
        values = {
            "category": "housing",
            "sub": "apts-housing",
            "title": "近捷運站採光兩房",
            "price": 28500,
            "district": "大安區",
            "status": Postpage.Status.ACTIVE,
            "seller": "Taipei Home",
            "description": "步行五分鐘到捷運站，家具齊全，歡迎預約看屋。",
            "views": 86,
        }
        values.update(overrides)
        return Postpage(**values)

    def test_example_post_and_optional_price_are_valid(self):
        self.make_post().clean_fields()
        self.make_post(price=None).clean_fields()

    def test_text_fields_limit_chinese_characters(self):
        self.make_post(category="中" * 20, title="中" * 80).clean_fields()

        with self.assertRaises(ValidationError):
            self.make_post(category="中" * 21).clean_fields()
        with self.assertRaises(ValidationError):
            self.make_post(description="中" * 4001).clean_fields()

    def test_price_and_views_enforce_upper_limits(self):
        self.make_post(price=9_999_999, views=99_999).clean_fields()

        with self.assertRaises(ValidationError):
            self.make_post(price=10_000_000).clean_fields()
        with self.assertRaises(ValidationError):
            self.make_post(views=100_000).clean_fields()

    def test_status_only_accepts_active_or_inactive(self):
        self.make_post(status=Postpage.Status.INACTIVE).clean_fields()

        with self.assertRaises(ValidationError):
            self.make_post(status="pending").clean_fields()
