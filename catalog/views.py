from django.shortcuts import render # render(): 템플릿과 모델을 이용해 HTML 파일을 생성하는 함수
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

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

class BookListView(generic.ListView):
    # Generic views는 templates/application_name/the_model_name_list.html 에서 템플릿을 찾는다
    model = Book # object_list 또는 book_list 템플릿 변수 사용 가능
    paginate_by = 2

    # 템플릿 변수명 바꾸고 싶을 때
    # context_object_name = 'my_book_list'

    # queryset = Book.objects.filter(title__icontains='war')[:5]
    #def get_queryset(self):
    #    return Book.objects.filter(title__contains="비포")[:5]

    def get_context_data(self, **kwargs):
        # 템플릿에 추가적인 변수를 전달하고 싶다면... (book_list는 디폴트로 전달)
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2

class AuthorDetailView(generic.DetailView):
    model = Author
