from django.db import models

class Articles(models.Model):
    title = models.CharField('Назва', max_length=100)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Стаття')
    image = models.ImageField('Зображення', default='img.jpg', upload_to='static/article_images/')
    date = models.DateField('Дата публікації')

    def __str__(self):
        return self.title
