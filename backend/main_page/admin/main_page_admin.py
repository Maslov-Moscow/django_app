from django.contrib import admin

from main_page.models.main_page import MainPage


from solo.admin import SingletonModelAdmin



@admin.register(MainPage)
class MainPageAdmin(SingletonModelAdmin):
    pass