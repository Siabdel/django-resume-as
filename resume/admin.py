from django.contrib import admin
from .models import Overview, PersonalInfo
from .models import Education, Job, JobAccomplishment
from .models import Skillset, Skill, ProgrammingArea, ProgrammingLanguage, Language
from .models import ProjectType, Project
from .models import Achievement, Publication

from . import models

# Register your models here.

class PersonalInfoAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('id', 'user', 'first_name','last_name','title','image','locality','region',)

class OverviewAdmin(admin.ModelAdmin): #customize appearance
    list_display = ['id', 'personal', 'text'] #otherwise it displays 'object'

class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'personal', 'name','name2', 'degree', 'formatted_end_date', 'location', 'description')
    list_filter = ('name','name2', 'degree', 'location')
    search_fields = ('name','name2', 'degree')
    #prepopulated_fields = {'slug': ('degree',)}
    date_hierarchy = 'end_date'
    ordering = ['-end_date', 'id']

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'personal', 'company', 'location', 'title', 'end_date')
    list_filter = ('company', 'location', 'title', 'end_date')
    search_fields = ('company', 'location', 'title')
    #prepopulated_fields = {'slug': ('degree',)}
    date_hierarchy = 'end_date'
    ordering = ['-end_date', 'id']
    #def __unicode__(self):
    #    return self.company

class JobAccomplishmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'personal', 'job', 'order', 'description')
    list_filter = ('job__company',)
    search_fields = ('job', )
    ordering = ['-job__end_date','order']
    
    #@property
    def job(self, obj):
        return obj.job.company
    
    job.short_description = 'Job'
    job.admin_order_field = 'job__end_date'
    #def __unicode__(self):
    #    return self.job.company

class SkillsetAdmin(admin.ModelAdmin):
    exclude = ()
    list_filter = ('name',)
    search_fields = ('name',)
    list_display = ( 'id', 'name',)

    #prepopulated_fields = {'slug': ('degree',)}
    ordering = ['name', 'id']

class SkillAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ( 'id', 'personal', 'get_skillset','order', 'text',)
    list_filter = ('skillset__name',)
    search_fields = ('skillset__name',)
    #prepopulated_fields = {'slug': ('degree',)}
    #date_hierarchy = 'order'
    ordering = ['skillset__name','order']
    def get_skillset(self, obj):
        return obj.skillset.name
    get_skillset.short_description = 'skillset'
    get_skillset.admin_order_field = 'skillset__name'

class ProgrammingAreaAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('name', 'order',)
    list_filter = ('name', )
    search_fields = ('name',)
    #prepopulated_fields = {'slug': ('degree',)}
    #date_hierarchy = 'order'
    ordering = ['order','name']

class ProgrammingLanguageAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('name', 'get_area', 'description',)
    list_filter = ('name',  'description', )
    search_fields = ('name',  'description', )
    #prepopulated_fields = {'slug': ('degree',)}
    ordering = ['programmingarea__name',]
    def get_area(self, obj):
        return obj.programmingarea.name

class LanguageAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('id', 'name', )
    list_filter = ('name',)
    search_fields = ('name', )
    #prepopulated_fields = {'slug': ('degree',)}
    #date_hierarchy = 'order'
    ordering = ['-name']

class ProjectTypeAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('name','order',)
    list_filter = ('name','order',)
    search_fields = ('name','order',)
    ordering = ['order','name']

class ProjectAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('id', 'personal', 'get_projtype','name','order','image','short_description','long_description')
    list_filter = ('projtype__name','name','order',)
    search_fields = ('projtype__name','name','order','image','short_description','long_description','link',)
    ordering = ['projtype__name','order']
    def get_projtype(self, obj):
        return obj.projtype.name

class AchievementAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('title','description','order','id','url','achievement_pdf')
    list_filter = ('title','url')
    search_fields = ('title','description','name',)
    #prepopulated_fields = {'slug': ('degree',)}
    #date_hierarchy = 'order'
    ordering = ['order','id']

class PublicationAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('title','year','order', 'journal',)
    list_filter = ('title','year','order', 'journal',)
    search_fields = ('title','year','journal',)
    #prepopulated_fields = {'slug': ('degree',)}
    #date_hierarchy = 'order'
    ordering = ['-year','order']


class MesLanguagesAdmin(admin.ModelAdmin):
    list_display = ('id','personal', 'language', 'level', 'order')


class MesProgrammingLanguagesAdmin(admin.ModelAdmin):
    list_display = ('id','personal', 'programming_language', 'level', 'order')

admin.site.register(models.MesLanguages, MesLanguagesAdmin)
admin.site.register(models.MesLanguageProgrammation, MesProgrammingLanguagesAdmin)


admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(Overview,OverviewAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobAccomplishment, JobAccomplishmentAdmin)
admin.site.register(Skillset, SkillsetAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(ProgrammingArea,ProgrammingAreaAdmin)
admin.site.register(ProgrammingLanguage, ProgrammingLanguageAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(ProjectType, ProjectTypeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Publication, PublicationAdmin)
