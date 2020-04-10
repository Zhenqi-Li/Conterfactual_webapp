from django.test import TestCase
from .views import choosecolor
from .models import Adult
from django.test import Client
# Create your tests here.
class responsetest(TestCase):
    def test1(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)
class viewstest(TestCase):
    def testcolor(self):
        num = 0.15
        color =  choosecolor(num)
        self.assertEqual(color, "#FF8469")
    def testdata(self):
        data = Adult.objects.create(Adultid=3, age=4)
        self.assertEquals(data.age, 4)



