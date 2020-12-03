# Use View Inheritance

Create a series of templates
    
    book_theme.html
    _header.html
    _footer.html
    _navbar.html
    _user.html
    
## book_theme.html

```html
    <!doctype html>
    <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>{{ page_title }}</title>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
                  integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z"
                  crossorigin="anonymous">
            <link rel="stylesheet" href="/static/shrinking-world.css">
        </head>

        <body class="bg-dark text-light">

            {% block content %}

                {% block header %}
                    {% include '_header.html' %}
                {% endblock header %}


                {% block navbar %}
                    {% include '_navbar.html' %}
                {% endblock navbar %}


                <main class="text-dark">
                    <div class="container py-5">

                        {% block main %}
                            <h2>NO MAIN DEFINED</h2>
                        {% endblock main %}

                    </div>
                </main>


                {% block footer %}
                    {% include '_footer.html' %}
                {% endblock footer %}

            {% endblock content %}

            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
                    integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
                    crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"
                    integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN"
                    crossorigin="anonymous"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"
                    integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV"
                    crossorigin="anonymous"></script>

        </body>

    </html>
```
    

## _header.html

```html
<header class="p-lg-5">

    <h1 class="display-4 ml-5">
        <a href="/">Book Builder</a>
    </h1>

    <h2 class="ml-5">An Author's Best Friend</h2>

</header>
```
    

## _footer.html

```html
<footer class="bg-primary p-3 text-center text-light">
    &copy;2020 -
    <b><a href="https://shrinking-world.com" class="text-light">Shrinking World</a></b>
    - Practical Software Engineering
</footer>
```
    

## _navbar.html

```html
<nav class="navbar navbar-expand-sm navbar-light bg-light mb-2">

    <div class="container">

        <button class="navbar-toggler" data-toggle="collapse" data-target="#navbarCollapse">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarCollapse">

            <a href="{% url 'home' %}" class="navbar-brand">Book Builder App</a>

            <ul class="navbar-nav ml-auto">

                {% for i in menu.menu_items %}
                    <li class="nav-item {{ i.active }}">
                        <a href="{{ i.url }}" class="nav-link">{{ i.label }}</a>
                    </li>
                {% endfor %}

                {% include '_user.html' %}

            </ul>

        </div>
    </div>

</nav>
```


## _user.html

```html
{% if user.is_authenticated %}
    <li class="nav-item active">
        <span class="nav-link p-2 m-2">Welcome {{ user.username }}</span>
    </li>
    <li class="nav-item">
        <a href="{% url 'logout' %}" class=" nav-link p-2 m-2">
            <i class="fas fa-sign-out-alt"></i> Log out
        </a>
    </li>
{% else %}
    <li class="nav-item">
        <span class="nav-link p-2 m-2">You are not logged in.</span>
    </li>

    <li class="nav-item active">
        <a href="{% url 'login' %}" class="nav-link p-2 m-2">
            <i class="fas fa-sign-in-alt"></i> Log In
        </a>
    </li>
{% endif %}
```

    