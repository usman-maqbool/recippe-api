from django.contrib.auth import get_user_model
from django.test import TestCase

class TestUser(TestCase):

    def test_user_is_created(self):

        email = "test@test.com"
        password = "testpass"
        user = get_user_model().objects.create_user(
            email = email, 
            password = password
        )
        self.assertEqual(user.email ,  email )
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        email = 'usman@Test.COM'
        user = get_user_model().objects.create_user(
            email = email, 
            password ='kkmskdsmk'
        )
        self.assertEqual(user.email  , email.lower())


    def test_new_user_invalid_email(self):
        
        """ Test for creating the user with no email """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None , 'emisdk')
         

