from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

# 모델 클래스 구성
# - Fields: Table의 Column
# - Meta 클래스: 다양한 옵션 사용 가능
# - Methods: def로 선언(__str__ 메서드 선언 필수)

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='책 장르를 입력하세요')

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200, help_text='책의 언어를 입력하세요')

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Book(models.Model):
    # 책 정보 포함(단 대여 관련 정보 포함x)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='간단한 책 설명을 입력하세요')
    isbn = models.CharField('ISBN', max_length=13, help_text='13자리 <a href="https://www.isbn-international.org/content/what-isbn">ISBN 숫자</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Book 모델의 세부 레코드에 접근하기 위한 URL
        # book-detail이라는 URL 매핑, 관련 뷰, 템플릿 정의 필요
        # (admin에서 VIEW ON SITE 버튼 활성화)
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    # short_description: admin에서 출력되는 field의 label 커스터마이징할 때 사용
    display_genre.short_description = 'Genre'

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='전체 도서관의 특정 책에 대한 고유한 ID')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='대여 상태'
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        # Python 3.6부터 사용되는 String formatting
        return f'{self.id} ({self.book.title})'

    

    