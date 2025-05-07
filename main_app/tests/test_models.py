from django.test import TestCase
from django.contrib.auth import get_user_model
from main_app.models import Map, Marker, Tag, Category, Comment
from datetime import datetime


class FlexiMapModelTests(TestCase):
    def setUp(self):
        
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')

        
        self.category1 = Category.objects.create(name="Cafés", description="Coffee & chill spots")
        self.category2 = Category.objects.create(name="Libraries", description="Study areas")

        
        self.tag1 = Tag.objects.create(name="Quiet")
        self.tag2 = Tag.objects.create(name="WiFi")

        
        self.map1 = Map.objects.create(name="Riyadh Map", description="Best places in Riyadh", created_by=self.user, category=self.category1)
        self.map2 = Map.objects.create(name="Study Spots", description="Library Map", created_by=self.user)

        
        self.map1.tags.set([self.tag1, self.tag2])

        self.marker1 = Marker.objects.create(map=self.map1, name="Starbucks", description="Great coffee", latitude=24.7136, longitude=46.6753, category=self.category1)
        self.marker2 = Marker.objects.create(map=self.map1, name="Library", description="Quiet place", latitude=24.7743, longitude=46.7386, category=self.category2)

    
        self.marker1.tags.set([self.tag2])

        
        self.comment1 = Comment.objects.create(marker=self.marker1, user=self.user, content="Very nice cafe!")
        self.comment2 = Comment.objects.create(marker=self.marker2, user=self.user, content="Loved the quiet space.")

    
    def test_user_created(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_category_creation(self):
        self.assertEqual(str(self.category1), "Cafés")
        self.assertEqual(str(self.category2), "Libraries")

    def test_tag_creation(self):
        self.assertEqual(str(self.tag1), "Quiet")
        self.assertEqual(str(self.tag2), "WiFi")

    def test_map_creation(self):
        self.assertEqual(str(self.map1), "Riyadh Map")
        self.assertEqual(self.map1.created_by, self.user)

    def test_marker_creation(self):
        self.assertEqual(str(self.marker1), "Starbucks")
        self.assertEqual(self.marker1.latitude, 24.7136)

    def test_comment_creation(self):
        self.assertEqual(str(self.comment1), "Comment by testuser on Starbucks")

   
    def test_map_tags_relationship(self):
        self.assertEqual(self.map1.tags.count(), 2)
        self.assertIn(self.tag1, self.map1.tags.all())

    def test_marker_tags_relationship(self):
        self.assertEqual(self.marker1.tags.count(), 1)
        self.assertIn(self.tag2, self.marker1.tags.all())

    def test_marker_map_relationship(self):
        self.assertEqual(self.marker1.map, self.map1)

    def test_comment_user_relationship(self):
        self.assertEqual(self.comment1.user, self.user)

    def test_comment_marker_relationship(self):
        self.assertEqual(self.comment2.marker, self.marker2)

   
    def test_delete_map_cascades_to_markers(self):
        self.assertEqual(Marker.objects.count(), 2)
        self.map1.delete()
        self.assertEqual(Marker.objects.count(), 0)

    def test_delete_marker_cascades_to_comments(self):
        self.assertEqual(Comment.objects.count(), 2)
        self.marker1.delete()
        self.assertEqual(Comment.objects.count(), 1)

    def test_delete_user_cascades_to_maps(self):
        self.assertEqual(Map.objects.count(), 2)
        self.user.delete()
        self.assertEqual(Map.objects.count(), 0)

# Create your tests here.
