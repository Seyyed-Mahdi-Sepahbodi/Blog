FROM python:3.8
LABEL MAINTAINER="Seyyed Mahdi Sepahbodi | seyyedmahdisepahbodi@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN mkdir /myBlog
WORKDIR /myBlog
COPY . /myBlog
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "myBlog", "--bind", ":8000", "myBlog.wsgi:application"]
