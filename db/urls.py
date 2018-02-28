
from django.conf.urls import url
from django.contrib import admin
from main.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', lista, name='lista'),

    url(r'^mysql/$', mysql_db, name='mysql-db'),    
    url(r'^mysql/listar/$', listar_tablas, name='listar_tablas'),
    url(r'^mysql/listar/campos/$', listar_tablas_campos_mysql, name='listar_tablas_campos_mysql'),
    url(r'^mysql/listar/campos/nombres/$', listar_tablas_nombres_campos_mysql, name='listar_tablas_nombres_campos_mysql'),

    url(r'^postgres/$', postgres_db, name='postgres-db'),
    url(r'^postgres/listar/$', listar_tablas_postgres, name='listar_tablas_postgres'),
    url(r'^postgres/listar/catalogo/$', listar_tablas_postgres_catalogo, name='listar_tablas_postgres_catalogo'),
    url(r'^postgres/listar/campos/$', listar_tablas_campos_postgres, name='listar_tablas_campos_postgres'),
    url(r'^postgres/listar/campos/nombres/$', listar_tablas_nombres_campos_postgres, name='listar_tablas_nombres_campos_postgres'),
]
