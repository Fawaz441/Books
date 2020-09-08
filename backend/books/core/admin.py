from django.contrib import admin
from .models import Book,Author

class BookInlineAdmin(admin.TabularInline):
    model = Book
    extra = 1

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','state']
    search_fields = ['first_name','last_name']
    inlines = [BookInlineAdmin]

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','published_date']


admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
