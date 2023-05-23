import idlelib.run

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Feedback
from .form import FeedbackForm
from django.http import HttpResponseRedirect


def first_page(request):
    obj = Movie.objects.values('id', 'name', 'raiting').filter(raiting__lt=90)
    print("objects: ", obj)
    content_object = Movie.objects.values()
    print("content_object:\n", content_object)
    context = {'obj': obj, 'content_object': content_object}
    return render(request, 'one_page.html', context)


def show_all_movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies/show_all_movies.html', {'movies': movies})


def show_one_movie(request, id_movie: int):
    movie = get_object_or_404(Movie, id=id_movie)
    return render(request, 'movies/show_one_movies.html', {'movie': movie})


def feedback(request):# вариант1 11.05.2023
    print('fb')
    form = FeedbackForm()
    print(form)
    print(request.method)
    if request.method == 'POST':
        print('POST')
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            feed=Feedback(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                feedback=form.cleaned_data['feedback']
            )
            feed.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm()
        print('qwerty')
        print(form.errors)
    return render(request, 'movies/feedback.html', context={'form': form})

'''
def feedback(request): # вариант2 данные из модели в форму
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm() 
    return render(request, 'movies/feedback.html', context={'form': form})

'''
def done(request):
    print('done')
    #objects_values = Feedback.objects.values()
    #print('objects_values:', objects_values)
    #return render(request, 'movies/table.html')
    return render(request, 'movies/done.html')

def table(request):
    print('table')
    #objects_values = Feedback.objects.values()
    #print('objects_values:', objects_values)
    fb_all = Feedback.objects.all()
    print('fb_all:', fb_all)

    x = Feedback.objects.filter(feedback__contains="ок") # рус
    print(x)
    x = Feedback.objects.filter(feedback__contains="ok") # анг
    print(x)
    x= Feedback.objects.filter(feedback__contains="ок") | Feedback.objects.filter(feedback__contains="ok") # или
    #WHERE("movieApp_feedback"."feedback"  LIKE '%ок%'   ESCAPE'\' OR "movieApp_feedback"."feedback" LIKE ' % ok % ' ESCAPE '\')
# (Abc.objects.filter(id__gte=17) & Abc.objects.filter(c__gte=15)).values('c').annotate(Count('id'))
    print(x.values())
    # колво отзывов ok
    col=x.count()
    # или 
    #col=(Feedback.objects.filter(feedback__contains="ок") | Feedback.objects.filter(feedback__contains="ok")).count()

    cur_objects = Feedback.objects.all()
    #statics_val = [cur_objects.aggregate(Count('b')), cur_objects.aggregate(Avg('b')), cur_objects.aggregate(Min('b')),
                   #cur_objects.aggregate(Max('b')), cur_objects.aggregate(StdDev('b')), cur_objects.aggregate(Sum('b'))]

    #print(statics_val)
    #statics = {'statics_val': statics_val}

    return render(request, 'movies/table.html', {'fb_all': fb_all, 'x':x, 'col':col})



'''
def one_page(request, pk):
    
   
    nav_objects = Movie.objects.values('id','item_nav', 'item_nav_position').filter(item_nav_position__gt=0).order_by('-item_nav_position')
    print("nav_objects: ", nav_objects)
    content_object = Movie.objects.values().get(id=pk)
    print("content_object:\n", content_object)
    context = {'pk': pk, 'nav_objects': nav_objects, 'content_object': content_object}
    return render(request, 'one_page.html', context)'''
