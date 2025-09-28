from django.contrib import admin
from .models import Category, Course, Topic, Lesson, CourseCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for the Category model.
    """
    list_display = ("id", "name", "description")
    search_fields = ("name",)
    ordering = ("name",)


class CourseCategoryInline(admin.TabularInline):
    """
    Inline for managing the relationship between Course and Category.
    """
    model = CourseCategory
    extra = 1


class TopicInline(admin.TabularInline):
    """
    Inline for managing Topics within a Course.
    """
    model = Topic
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Admin interface for the Course model.
    """
    list_display = ("id", "title", "duration", "is_active", "is_premium")
    list_filter = ("is_active", "is_premium")
    search_fields = ("title", "description")
    inlines = [CourseCategoryInline, TopicInline]


class LessonInline(admin.TabularInline):
    """
    Inline for managing Lessons within a Topic.
    """
    model = Lesson
    extra = 1


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    Admin interface for the Topic model.
    """
    list_display = ("id", "title", "course")
    list_filter = ("course",)
    search_fields = ("title", "content")
    inlines = [LessonInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Admin interface for the Lesson model.
    """
    list_display = ("id", "title", "topic", "video", "document")
    list_filter = ("topic",)
    search_fields = ("title",)


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for the CourseCategory model (intermediate table)
    ."""
    list_display = ("id", "course", "category")
    list_filter = ("category", "course")
    search_fields = ("course__title", "category__name")
