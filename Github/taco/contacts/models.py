from django.db import models

# Create your models here.

class Contact(models.Model):
    contacts_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    contacts_name = models.CharField(max_length=50, verbose_name='Имя')
    contacts_email = models.EmailField(verbose_name='Email')
    contacts_text = models.TextField()
    contacts_called = models.BooleanField(default=False, verbose_name='Звонок')

    def __str__(self):
        return self.contacts_name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['contacts_date',]

class MenuCategory(models.Model):
    category_name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = 'Категория меню'
        verbose_name_plural = 'Категории меню'

class MenuName(models.Model):
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=50)

    def __str__(self):
        return self.menu_name

class MenuPrice(models.Model):
    price_name = models.ForeignKey(MenuName, on_delete=models.CASCADE)
    price_quant = models.IntegerField()
    price_price = models.TextField(max_length=50)