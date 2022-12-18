from django.test import TestCase 
from ..models import *

class test_university(TestCase):
    def setUp(self):
        """usr=user.objects.create(username="1111",email="test@test.test",password="test")
        pf=portfolio.objects.create(usr_id=usr.id)
        skill.objects.create(portfolio_id=pf.id,name='data',tool='python')
        #University.objects.create(name='IHEC',location='Carthage')"""
        
    def test_univ_obj(self):
        my_skill=skill.objects.get(name='data')
        self.assertEqual(my_skill.tool,'python')
        self.assertIsInstance(my_skill.tool,str) # verify que loc est une chaine de char