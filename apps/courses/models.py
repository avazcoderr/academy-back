from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from utils import AbstractBaseModel


def lesson_video_path(instance, filename):
    lesson_slug = slugify(instance.title)
    return f"lessons/videos/{lesson_slug}/{filename}"



class Category(AbstractBaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]
        db_table = "categories"
        indexes = [
            models.Index(fields=["name"]),
        ]


class Course(AbstractBaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in hours")
    is_active = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ["-created_at"]
        db_table = "courses"


class CourseCategory(AbstractBaseModel):
    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        related_name="course_categories"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="category_courses"
    )

    class Meta:
        verbose_name = "Course Category"
        verbose_name_plural = "Course Categories"
        unique_together = ("course", "category")
        db_table = "course_categories"
        indexes = [
            models.Index(fields=["course", "category"]),
        ]

    def __str__(self):
        return f"{self.course.title} -> {self.category.name}"


class Topic(AbstractBaseModel):
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        related_name="topics"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"
        ordering = ["course"]
        db_table = "topics"


class Lesson(AbstractBaseModel):
    topic = models.ForeignKey(
        Topic, 
        on_delete=models.CASCADE, 
        related_name="lessons"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    video = models.FileField(
        upload_to=lesson_video_path,
        validators=[FileExtensionValidator(allowed_extensions=["mp4", "avi", "mov"])],
        null=True,
        blank=True
    )
    document = models.FileField(
        upload_to="lessons/documents/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "docx", "pptx"])],
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.topic.title} - {self.title}"

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"
        ordering = ["topic"]
        db_table = "lessons"
        indexes = [
            models.Index(fields=["topic", "title"]),
        ]