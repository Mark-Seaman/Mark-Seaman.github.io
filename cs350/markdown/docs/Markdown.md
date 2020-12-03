# Markdown Text Display

Add markdown text documents and display them as HTML.


## Virtual Environment

Create a virtual environment that includes markdown package.

    python3 --version
    Python 3.8.6
    
    # Install a Python 3 enviroment
    python3 -m venv .venv
    
    # Activate environment
    source .venv/bin/activate
    
    # Install packages
    pip install django pillow markdown django-crispy-forms requests
    
    # List packages
    pip freeze
    
    
## Markdown Test

Run code by itself

markdown.py
    
    from markdown import markdown
    
    print(markdown('# Headline\n\nParagraph 1\n\nParagraph 2'))
    
    
tests.py

    from markdown import markdown
    from django.test import SimpleTestCase

    class MarkdownTests(SimpleTestCase):
        
        def test_markdown(self):
            actual = markdown('# Headline\n\nParagraph 1\n\nParagraph 2')
            expected = '<h1>Headline</h1>\n<p>Paragraph 1</p>\n<p>Paragraph 2</p>'
            self.assertEqual(actual, expected)

## Data Model

Add text field to data model

    class Chapter(models.Model):
        book = models.ForeignKey(Book, on_delete=models.CASCADE, editable=False)
        title = models.CharField(max_length=100)
        chapter_num = models.IntegerField()
        text = models.TextField(default='No Chapter Text')
    

Migrate the database

    python manage.py makemigrations
    
    python manage.py migrate
    

Run the server 

    python manage.py runserver
    
    browse to http://127.0.0.1:8000/
    

## View

templates/chapter_edit.html

    {% extends 'book_theme.html' %}

    {% block main %}
        <form action="" method="post">{% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Save</button>
        </form>
    {% endblock main %}


templates/chapter_detail.html

    {% extends 'book_theme.html' %}
    
    {% block main %}
        <div class="card m-3">
           <div class="card-header bg-light text-dark">
               {{ chapter.title }}
           </div>
           <div class="card-body bg-dark text-light">
               {% autoescape off %}
                   {{ markdown }}
               {% endautoescape %}
           </div>
        </div>
        <a href="{{ chapter.pk }}/" class="btn btn-success m-3">Edit Chapter</a>
    {% endblock main %}


views.py    

    class ChapterEdit(UpdateView):
        template_name = "chapter_edit.html"
        model = Chapter
        fields = '__all__'
        
    
    class ChapterDetail(DetailView):
        template_name = 'chapter_detail.html'
        model = Chapter
        
        def get_context_data(self, **kwargs):
            kwargs = super().get_context_data(**kwargs)
            kwargs['markdown'] = markdown(kwargs['object'].text)
            return kwargs

