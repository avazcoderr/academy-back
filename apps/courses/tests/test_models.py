from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.courses.models import Category, Course, Topic, Lesson, CourseCategory


class TestCategoryModel(TestCase):
    """
    Tests for the Category model.
    """

    def setUp(self):
        self.category = Category.objects.create(
            name="Programming",
            description="Programming related courses"
        )

    def test_str_representation(self):
        self.assertEqual(str(self.category), "Programming")

    def test_meta_options(self):
        self.assertEqual(self.category._meta.verbose_name, "Category")
        self.assertEqual(self.category._meta.verbose_name_plural, "Categories")
        self.assertEqual(self.category._meta.db_table, "categories")


class TestCourseModel(TestCase):
    """
    Tests for the Course model.
    """

    def setUp(self):
        self.category = Category.objects.create(name="Math")
        self.course = Course.objects.create(
            title="Algebra Basics",
            description="Introduction to Algebra",
            duration=40,
            is_active=True,
            is_premium=False,
        )
        # Create link manually
        CourseCategory.objects.create(course=self.course, category=self.category)

    def test_str_representation(self):
        self.assertEqual(str(self.course), "Algebra Basics")

    def test_course_has_category(self):
        link = CourseCategory.objects.filter(course=self.course, category=self.category)
        self.assertTrue(link.exists())

    def test_meta_options(self):
        self.assertEqual(self.course._meta.verbose_name, "Course")
        self.assertEqual(self.course._meta.verbose_name_plural, "Courses")
        self.assertEqual(self.course._meta.db_table, "courses")


class TestTopicModel(TestCase):
    """
    Tests for the Topic model.
    """

    def setUp(self):
        self.course = Course.objects.create(
            title="History 101",
            description="Basic history course",
            duration=20
        )
        self.topic = Topic.objects.create(
            course=self.course,
            title="Ancient Civilizations",
            content="Egypt, Mesopotamia, etc."
        )

    def test_str_representation(self):
        self.assertEqual(
            str(self.topic),
            f"{self.course.title} - {self.topic.title}"
        )

    def test_meta_options(self):
        self.assertEqual(self.topic._meta.verbose_name, "Topic")
        self.assertEqual(self.topic._meta.verbose_name_plural, "Topics")
        self.assertEqual(self.topic._meta.db_table, "topics")


class TestLessonModel(TestCase):
    """
    Tests for the Lesson model.
    """

    def setUp(self):
        self.course = Course.objects.create(
            title="Physics",
            description="Physics basics",
            duration=50
        )
        self.topic = Topic.objects.create(
            course=self.course,
            title="Mechanics",
            content="Newton's laws"
        )
        self.lesson = Lesson.objects.create(
            topic=self.topic,
            title="Newton’s First Law",
            video=SimpleUploadedFile("video.mp4", b"file_content", content_type="video/mp4"),
            document=SimpleUploadedFile("doc.pdf", b"file_content", content_type="application/pdf"),
        )

    def test_str_representation(self):
        self.assertEqual(
            str(self.lesson),
            f"{self.topic.title} - {self.lesson.title}"
        )

    def test_meta_options(self):
        self.assertEqual(self.lesson._meta.verbose_name, "Lesson")
        self.assertEqual(self.lesson._meta.verbose_name_plural, "Lessons")
        self.assertEqual(self.lesson._meta.db_table, "lessons")


class TestCourseCategoryModel(TestCase):
    """
    Tests for the CourseCategory model.
    """

    def setUp(self):
        self.category = Category.objects.create(name="Science")
        self.course = Course.objects.create(
            title="Biology",
            description="Biology basics",
            duration=25
        )
        self.course_category = CourseCategory.objects.create(
            course=self.course,
            category=self.category
        )

    def test_str_representation(self):
        self.assertEqual(
            str(self.course_category),
            f"{self.course.title} -> {self.category.name}"
        )

    def test_unique_together(self):
        """
        Should not allow duplicate course-category pairs.
        """
        with self.assertRaises(Exception):
            CourseCategory.objects.create(
                course=self.course,
                category=self.category
            )

    def test_meta_options(self):
        self.assertEqual(self.course_category._meta.db_table, "course_categories")
