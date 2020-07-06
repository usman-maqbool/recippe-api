from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase

class CommandTest(TestCase):

    def test_wait_db_to_ready(self):
        """ Test waiting for the db when db is available""" 
        