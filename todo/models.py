from django.db import models

# Create your models here.
class News(models.Model):

    """
    Это модель описыввает структуру в базе данных
    """

    title = models.CharField(max_length=50)
    desc = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self)-> str:
        return f'id:{self.id} {self.title}'
    

