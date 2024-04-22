import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_default_constructor(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_constructor_with_id(self):
        b2 = Base(10)
        self.assertEqual(b2.id, 10)

    def test_multiple_instances(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)
        self.assertEqual(b3.id, 4)

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 1}]), '[{"id": 1}]')

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{'id': 1}])


if __name__ == '__main__':
    unittest.main()
