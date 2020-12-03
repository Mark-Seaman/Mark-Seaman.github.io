# View Workshop

### blogging application
* Build a blogging application
* Copy code from previous demo to Demo29


### 1. Workshop
* Add workshop app to project

    python manage.py startapp workshop


* templates/workshop.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Workshop View</title>
</head>
<body>
    <h1> View Workshop</h1>
    <p>
        This page is to demonstrate how to build complex views with many layers.
        Django makes it easy to composite view that are driven by data.
    </p>
</body>
</html>
```


* workshop/views.py

```python
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'workshop.html'
    
```


* workshop/urls.py

```python
    from django.urls import path
    from .views import HomeView

    urlpatterns = [
        path('',  HomeView.as_view(),   name='workshop'),
    ]
```


* config/urls.py

```python
    from django.urls import path, include

    urlpatterns = [
        path('', include('accounts.urls')), 
        path('', include('blog.urls')),
        path('workshop/', include('workshop.urls'))
    ]
```


### 2. Container

* Add container to view
* templates/workshop.html

```html
<div class="container">
    <h1> View Workshop</h1>
    <p>
        This page is to demonstrate how to build complex views with many layers.
        Django makes it easy to composite view that are driven by data.
    </p>
</div>
<p>
    This text is outside of the container.
</p>
```


### 3. Grid Layout 
* Add "row" and "col"
* A row will fit items horizontally
* Start with equal width
* templates/workshop.html

```html
<div class="container">
   <div class="row">
       <div class="col"> {{ text }} </div>
       <div class="col"> {{ text }} </div>
       <div class="col"> {{ text }} </div>
   </div>
</div>
```


* workshop/views.py

```python
from django.views.generic import TemplateView
random_text = '...'

class HomeView(TemplateView):
    template_name = 'workshop.html'
    
    def get_context_data(self, **kwargs):
        return dict(text=random_text)

```


### 4. Responsive Columns

* Use class "col-lg-4, col-lg-8"
* Color the first column
* Test the response to resizing the view
* templates/workshop.html

```html
<div class="container">
    <div class="row">
        <div class="col-lg-4 bg-dark text-light"> {{ text }} </div>
        <div class="col-lg-8"> {{ text }} </div>
    </div>
</div>
```


### 5. Card Layout

* Use class "col-lg-6" for half width
* Test the response to resizing the view
* templates/workshop.html

```html
<div class="col-lg-6">
    <div class="card">
        <div class="card-header bg-primary text-light">
            <h2>Card</h2>
        </div>
        <div class="card-body">
            <p>{{ text }}</p>
        </div>
    </div>
</div>
```


### 6. Multiple Card Layout

* Use class "col-lg-6" for half width
* Iterate over all cards
* templates/workshop.html

```html
{% for card in cards %}
                
    <div class="col-lg-6">
        <div class="card">
            <div class="card-header bg-primary text-light">
                <h2>{{ card.title }}</h2>
            </div>
            <div class="card-body">
                <p>{{ card.body }}</p>
            </div>
        </div>
    </div>

{% endfor %}
```

* workshop/views.py

```python
from django.views.generic import TemplateView
random_text = '...'

class HomeView(TemplateView):
    template_name = 'workshop.html'
    
    def get_context_data(self, **kwargs):
        return {'cards': [
            dict(title="Card 1", body=text),
            dict(title="Card 2", body=text),
        ]}

```


### 7. Columns of Cards

* Pass in a list of columns
* Each column is a list of cards
* templates/workshop.html

```html
{% for column in columns.cards %}

    <div class="card">
        <div class="card-header">
            {{ column.header }}
        </div>
        <div class="card-body">
            {{ column.body }}

            <div class="row">

                {% for card in column.cards %}
                    <div class="col-md-6">
                        <div class="card">
                            <div class="card-header">
                                {{ card.header }}
                            </div>
                            <div class="card-body">
                                {{ card.body }}
                            </div>

                        </div>
                    </div>
                {% endfor %}
            </div>
        </div>
    </div>

{% endfor %}
```

* workshop/views.py

```python
from django.views.generic import TemplateView
random_text = '...'

class HomeView(TemplateView):
    template_name = 'workshop.html'
    
    def get_context_data(self, **kwargs):
        return {'cards': [
            dict(title="Card 1", body=text),
            dict(title="Card 2", body=text),
        ]}

```


### 8. Accordion

### 9. Tabbed View

### 10. Includes

### 11. Composite View



