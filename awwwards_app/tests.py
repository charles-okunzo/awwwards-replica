from django.test import TestCase
from django.contrib.auth.models import User
from awwwards_app.models import Project, Rating

# Create your tests here.


class ProjectTestClass(TestCase):
    def setUp(self):
        self.new_user = User(email = 'abc@gmail.com', username = 'Abc254', password = 'test123')
        self.new_project = Project(user=self.new_user, 
        title='My project', 
        image='/profile_pic/image.jpg', 
        description='This project is great',
        link='www.project.com'
        )

    def test_instance(self):
        '''
        Test class that tests if the object is an instance of the class.
        '''
        self.assertTrue(isinstance(self.new_project, Project))

    def test_save(self):
        self.new_user.save()
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete(self):
        self.new_user.save()
        self.new_project.save_project()
        self.new_project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)<1)

class RatingTestClass(TestCase):
    def setUp(self):
        self.new_user = User(email = 'abc@gmail.com', username = 'Abc254', password = 'test123')
        self.new_project = Project(
            user=self.new_user, 
            title='My project', 
            image='/profile_pic/image.jpg', 
            description='This project is great',
            link='www.project.com'
        )

        self.new_rating=Rating(
            design=7,
            usability=8,
            content=9,
            user=self.new_user,
            project = self.new_project
        )

    def test_instance(self):
        '''
        Test class that tests if the object is an instance of the class.
        '''
        self.assertTrue(isinstance(self.new_rating, Rating))

    def test_save(self):
        self.new_user.save()
        self.new_project.save_project()
        self.new_rating.save_rating()
        ratings = Rating.objects.all()
        self.assertTrue(len(ratings)>0)

    def test_delete(self):
        self.new_user.save()
        self.new_project.save_project()
        self.new_rating.save_rating()
        self.new_rating.delete_rating()
        ratings = Rating.objects.all()
        self.assertTrue(len(ratings)<1)