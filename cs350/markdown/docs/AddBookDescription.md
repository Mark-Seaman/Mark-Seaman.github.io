# Add Description for book
* Detail View pass in markdown HTML and display
* Modify book/models.py
* Modify book/views.py
* Modify templates/book_detail.html
* Modify book/tests.py


## book/models.py

```python
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
```


## templates/book_detail.html

```html
{% extends 'book_theme.html' %}

{% block main %}

    <h1>{{ book.title }}</h1>
    <h2>by {{ book.author.name }}</h2>

    <h3>About {{ book.title }}</h3>
    <p>
         {% autoescape off %}
             {{ markdown }}
         {% endautoescape %}
    </p>

    <div class="card">
        <div class="card-header">
            <h3>Chapters</h3>
        </div>
        <div class="card-body">
            <ul>
                {% for chapter in chapters %}
                    <li>
                        <a href="/chapter/{{ chapter.pk }}">{{ chapter }}</a>
                    </li>
                {% endfor %}
            </ul>
        </div>
    </div>

{% endblock main %}
```


## book/views.py

```python

class BookDetail(DetailView):
    template_name = 'book_detail.html'
    model = Book

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['chapters'] = Chapter.objects.filter(book=kwargs['object'])
        kwargs['markdown'] = markdown(kwargs['object'].description)
        return kwargs
    
```


## book/tests.py

```python

class BookTests(TestCase):

    def check_description(self, pk, text):
        b = Book.objects.get(pk=pk)
        self.assertEqual(b.description, text)

    def test_description(self):
        self.check_description(1, None)
        a = get_book('Tale of Two Cities')
        a.description = 'This is a book description'
        a.save()
        self.check_description(1, 'This is a book description')

```


## Test

    dj test
    
    dj runserver
    
