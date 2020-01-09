from django.shortcuts import render # render(): 템플릿과 모델을 이용해 HTML 파일을 생성하는 함수
from catalog.models import Book, Author, BookInstance, Genre

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    
    num_genres_contain_romance = Genre.objects.filter(name__contains='로맨스').count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres_contain_romance': num_genres_contain_romance
    }
    
    return render(request, 'index.html', context=context)

