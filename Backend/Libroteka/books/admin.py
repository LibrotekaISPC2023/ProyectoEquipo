from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Book
from .models import Author
from .models import User
from .models import Editorial
from .models import Genre
from .models import Order
from .models import OrderStatus

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'id_Author', 'id_Genre', 'id_Editorial', 'description', 'price', 'stock')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

class EditorialAdmin(admin.ModelAdmin):
    list_display = ('name',)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre',)

class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('status',)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id_Order_Status', 'id_User', 'date', 'books', 'total', 'books_amount')
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'password', 'dni', 'telephone', 'province', 'city', 'address')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Editorial, EditorialAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
