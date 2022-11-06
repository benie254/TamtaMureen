from django.contrib import admin
from tam_app.models import Super,ingredient,Menu,Quote

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    filter_horizontal=('ingredients',)


admin.site.register(Super)
admin.site.register(ingredient)
admin.site.register(Menu,MenuAdmin)
admin.site.register(Quote)
