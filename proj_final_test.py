from proj_final import *
import unittest

class TestFacebook(unittest.TestCase):
    def test_initialization(self):
        self.fb_data = Facebook_Scan(secrets.fb_access_token)
    def setUp(self):
        sample_file = open('Facebook_Cache_File.json')
        sample_text = sample_file.read()
        sample_file.close()
        sample_post_dict = json.loads(sample_text)
        self.post = Facebook_Scan(secrets.fb_access_token)

    def test_comments_1(self):
        self.assertIsInstance(self.post)

    def testing_DB_length(self, Facebook_Data):
        self.assertEqual(len(self.Facebook_Data),31)

    def test_FB_DB(self):
        self.assertIsInstance(sample_post_dict, ['Monday', 2, 0])


class TestInstagram(unittest.TestCase):
    def test_initialization(self):
        self.Instagram_data = get_instagram_data(secrets.ig_access_token)

    def test_Insta_DB_length(self):
        self.assertEqual(len(self.Instagram_data) >= 1)

    def test_Insta_DB_1(self):
        self.Instagram_data = get_instagram_data(secrets.ig_access_token)

    def test_Insta_DB_content(self):
        self.assertEqual(self.Instagram_data[0], ["346750066", 42, "Thursday"])




unittest.main()
