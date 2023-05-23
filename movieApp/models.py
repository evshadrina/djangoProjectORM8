from django.db import models
from django.urls import reverse
# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=40, default='Имя1')
    surname = models.CharField(max_length=60)
    feedback = models.TextField()

    def __str__(self):
       return f' Отзыв {self.name} -  {self.surname} -{self.feedback} '

class Movie(models.Model):
    name = models.CharField(max_length=100)
    raiting = models.IntegerField()

    def get_url(self):
        return reverse('movieApp:movie-detail', args=[self.id])
    #  ф-я нужна если в шаблоне вот так
    #  <li>  <a href="{{movie.get_url}}"> {{ movie.name}} </a>, рейтинг-{{ movie.raiting }}  </li>

    def __str__(self):
       return f' Фильм {self.name} - Рейтинг {self.raiting} '

    #python     manage.py     shell_plus - -print - sql
    # from movieApp.models import Movie
    #Movie(name='Чебурашка', raiting='100').save()

