# Инструкция по запуску

1. Необходимо скачать и запутить Docker Desktop 
2. В файле settings.py прописать настройки БД для mysql
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'name',
          'USER': 'user',
          'PASSWORD': 'password',
          'HOST': '127.0.0.1',
          'PORT': '8888'
      }
  }
3. На командной строке перейти в директорию проекта 
4. Выполнить команду 
  docker-compose up
