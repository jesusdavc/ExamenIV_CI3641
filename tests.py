import unittest
from classmanager import ClassManager
class TestClassManager(unittest.TestCase):
    def setUp(self):
        self.manager = ClassManager()

    def test_define_class_no_inheritance(self):
        self.manager.define_class("CLASS A f g")
        self.assertIn("A", self.manager.classes)
        self.assertEqual(self.manager.classes["A"], {"superclass": None, "methods": ["f", "g"]})

    def test_define_class_with_inheritance(self):
        self.manager.define_class("CLASS A f g")
        self.manager.define_class("CLASS B : A h i")
        self.assertIn("B", self.manager.classes)
        self.assertEqual(self.manager.classes["B"], {"superclass": "A", "methods": ["h", "i"]})

    def test_inheritance_cycle(self):
        self.manager.define_class("CLASS A f g")
        self.manager.define_class("CLASS B : A h i")
        with self.assertRaises(ValueError):
            self.manager.define_class("CLASS A : B j")

    def test_duplicate_methods(self):
        with self.assertRaises(ValueError):
            self.manager.define_class("CLASS A f f")

    def test_describe_class(self):
        self.manager.define_class("CLASS A f g")
        self.manager.define_class("CLASS B : A h i")
        vtable = {}
        self.manager._build_vtable("B", vtable)
        self.assertEqual(vtable, {
            "f": "A::f",
            "g": "A::g",
            "h": "B::h",
            "i": "B::i"
        })

    def test_describe_nonexistent_class(self):
        with self.assertRaises(ValueError):
            self.manager.describe_class("C")

if __name__ == "__main__":
    unittest.main()