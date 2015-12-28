from django.contrib import admin
from .models import Event, Category, Assistant, Comments
from .actions import export_xls
# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ('organizer','name','summary', 'category', 'start', 'finish')
	search_field = ('name', 'category')
	list_filter = ('category',)
	ordering = ('start',)
	actions = [export_xls]
	
	fieldsets = (
			('Event Info', {'fields': ('name', 'summary', 'content', 'place', 'category', 'imagen', 'views')}),
			('Fechas', {'fields': ('start', 'finish')}),
			('Pagos', {'fields': ('is_free', 'amoun')}),
			('Organizador(es)', {'fields': ('organizer',)}),
		)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_field = ('name',)
	list_filter = ('name',)
	ordering = ('name',)

	fieldsets = (
			('Nombre de Categoria', {'fields': ('name',)}),
		)

@admin.register(Assistant)
class AssistantAdmin(admin.ModelAdmin):
	list_display = ('assistant', 'has_paid', 'attended')
	search_field = ('attended',)
	list_filter = ('attended',)
	ordering = ('event',)
	filter_horizontal = ('event',)

	fieldsets = (
			('Assistant Info', {'fields': ('assistant','event','has_paid','attended')}),
		)

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
	list_display = ('content', 'event', 'user')
	search_field = ('user',)
	list_filter = ('user',)
	ordering = ('user',)

	fieldsets = (
			('Comentarios', {'fields': ('user','event','content')}),
		)




