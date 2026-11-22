from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from courses.models import Course, Category, Lesson, Tag
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'description']
    readonly_fields = ['avatar']
    def avatar(self, obj):
        if obj:
            return mark_safe('<img src="/static/{url}" width="120" />'\
            .format(url=obj.image.name)
            )

class CourseAppAdminSite(admin.AdminSite):
    site_header = "Hệ thống khóa học trực tuyến"

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonTagInlineAdmin(admin.TabularInline):
    model = Lesson.tag.through
    extra = 3


class LessonAdmin(admin.ModelAdmin):
    form = LessonForm
    list_display = ['id', 'subject', 'created_date', 'course']
    list_filter = ['subject', 'created_date']
    search_fields = ['subject', 'course__subject']
    readonly_fields = ['image_view']
    def image_view(self, lesson):
        return mark_safe(f'<img src="/static/{lesson.image.name}" width="150" />')

    class Media:
        css = {
            'all': ('/static/css/styles.css', )
        }

    inlines = [LessonTagInlineAdmin]

class TagAdmin(admin.ModelAdmin):
    inlines = [LessonTagInlineAdmin]

# admin.site = CourseAppAdminSite(name="myadmin")

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Category)
admin.site.register(Tag, TagAdmin)
