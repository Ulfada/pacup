import unittest
from configuration.tagged_package_list import TaggedPackageList

class TestTaggedPackageList(unittest.TestCase):
    def setUp(self):
        self.package_list = TaggedPackageList()

    def test_init_with_file_content(self):
        self.package_list.init_with_file_content(
            """
            a@1 e f g a


            b@2 
            c@3 tag

            """
        )
        self.assertEqual(3, len(self.package_list.tagged_packages))
        self.assertEqual("a", self.package_list.tagged_packages[0].name)
        self.assertEqual("b", self.package_list.tagged_packages[1].name)
        self.assertEqual("c", self.package_list.tagged_packages[2].name)
    
    def test_duplicate_init_with_file_content(self):
        err = False
        try:
            self.package_list.init_with_file_content(
                """
                a@1 e f g a
                a@1 sdf sf 
                """
            )
        except ValueError:
            err = True
        self.assertTrue(err)
