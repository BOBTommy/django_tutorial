from django.contrib import admin
from polls.models import *
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    #Inline Model -> parent - child structure
    #Admin can modify child's model in parent modification page

class PollAdmin(admin.ModelAdmin):

    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']

    fieldsets = [
        ('Questions',           {'fields' : ['question']}),
        ('Date information',    {'fields' : ['pub_date'], 'classes' : ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll,PollAdmin)
