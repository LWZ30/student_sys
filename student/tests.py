from django.test import TestCase,Client

from .models import Student

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='the5file',
            sex=1,
            email='sss@sdf.com',
            profession='程序员',
            qq='333333',
            phone='2222',
            )
    def test_create_and_sex_show(self):
        student=Student.objects.create(
            name='huyang',
            sex=1,
            email='sfsdf@sfd.com',
            prefession='外卖员',
            qq='333',
            phone='222',
            )
        self.asserEqual(student.sex_show,'男','性别内容跟展示一致')
    def test_filter(self):
        Student.objects.create(
            name='huawei',
            sex=1,
            email='sfsdf@sfs1.com',
            profession='厨师',
            qq='444444',
            phone='2222,'
            )
        name='the5file'
        sutdents=Student.objects.filter(name=name)
        self.asserEqual(students.count(),1,'应该只存在一个名称为{}的记录'.format(name))