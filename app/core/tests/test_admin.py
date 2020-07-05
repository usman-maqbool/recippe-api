from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AdminsiteTest(TestCase):

    def setUp(self):
        """ Users setup """
        self.client = Client()
        self.admin_user  = get_user_model().objects.create_superuser(
            email = 'test@test.com', 
            password = '123434dfd'
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email = 'test@testt.com', 
            password = 'tskdksldks' , 
            name = 'Testuser'
        )


    def test_users_listed(self):
        url  = reverse('admin:core_user_changelist')
        res  = self.client.get(url)
        
        self.assertContains(res , self.user.name)
        self.assertContains(res , self.user.email)
    

    def test_user_edit_page(self):
        """ Test that edit user page works """
        url = reverse('admin:core_user_change' , args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code , 200 )


    def test_create_user_page(self):
        """ Test that create user page works """
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code , 200)
    