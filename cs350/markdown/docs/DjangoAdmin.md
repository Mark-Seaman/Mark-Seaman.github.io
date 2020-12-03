# Python / Django install issues

Check out this tip offered by Ben McEwen

    py -m pip install –upgrade pip

If you have several Python versions installed on your machine and you have a project that is using the previous version of Python using virtual environment e.g. (venv) you can upgrade Python just in that venv using:

    python -m venv --upgrade "your virtual environment path"

For instance, I have Python 3.7 in my ./venv virtual environment and I would like upgrade venv to Python 3.8, I would do following

    python -m venv --upgrade ./venv

    python -m pip install Django or py -m pip install Django

Current Python 3 installations come with the py.exe launcher, which by default is installed into the system directory. This makes it available from the PATH, so you can automatically run it from any shell just by using py instead of python as the command. This avoids you having to put the current Python installation into PATH yourself. That way, you can easily have multiple Python installations side-by-side without them interfering with each other.

From:
https://docs.djangoproject.com/en/3.1/faq/troubleshooting/#troubleshooting-django-admin (Links to an external site.)

    command not found: django-admin¶

django-admin should be on your system path if you installed Django via pip. If it’s not in your path, ensure you have your virtual environment activated and you can try running the equivalent command python -m django.

Hope this helps Ben McEwen
