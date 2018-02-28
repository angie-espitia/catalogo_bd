# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json

import MySQLdb
import psycopg2

def lista(request):

	return render(request, 'index.html')

def mysql_db(request):
	db = MySQLdb.connect(user='root', db='mysql', passwd='1234567', host='localhost')
	cursor = db.cursor()
	cursor.execute('SHOW databases')
	nombres = [row[0] for row in cursor.fetchall()]
	db.close()

	return render(request, 'mysql.html', {'nombres': nombres})

def postgres_db(request):
	db2 = psycopg2.connect(user='postgres', dbname='postgres', password='1234567', host='localhost')
	cursor = db2.cursor()
	cursor.execute('select datname from pg_database')
	nombres2 = [row[0] for row in cursor.fetchall()]
	db2.close()

	return render(request, 'postgres.html', {'nombres2': nombres2})


def listar_tablas(request):
	db = MySQLdb.connect(user='root', db='mysql', passwd='1234567', host='localhost')
	cursor = db.cursor()
	value = request.POST.get('value')
	query = "show tables from %s" %value
	cursor.execute(query)
	tablas = [row[0] for row in cursor.fetchall()]
	dict = {'tablas':tablas}
	db.close()

	return HttpResponse(json.dumps(dict), content_type='application/json')

def listar_tablas_campos_mysql(request):
	dbs = request.POST.get('db')
	db = MySQLdb.connect(user='root', db=dbs, passwd='1234567', host='localhost')
	cursor = db.cursor()
	value = request.POST.get('value')
	query = "select * from %s" %value
	cursor.execute(query)
	dict = {}
	for row in cursor:
		print row
		dict.setdefault(row[0],row[1:])
	print dict
	db.close()

	return HttpResponse(json.dumps(dict), content_type='application/json')

def listar_tablas_nombres_campos_mysql(request):
	dbs = request.POST.get('db')
	db = MySQLdb.connect(user='root', db=dbs, passwd='1234567', host='localhost')
	cursor = db.cursor()
	value = request.POST.get('value')
	query = "DESCRIBE %s " % (value)
	cursor.execute(query)
	nombres_campos = [row[0] for row in cursor.fetchall()]
	dict = { 'nombres_campos' : nombres_campos }
	db.close()

	return HttpResponse(json.dumps(dict), content_type='application/json')

def listar_tablas_postgres(request):
	
	value = request.POST.get('value')
	db = psycopg2.connect(user='postgres', dbname=value, password='1234567', host='localhost')
	cursor = db.cursor()
	query = "select table_name from information_schema.tables where table_schema = 'public'"
	cursor.execute(query)
	tablas2 = [row[0] for row in cursor.fetchall()]
	dict = {'tablas2':tablas2}
	db.close()

	return HttpResponse(json.dumps(dict), content_type='application/json')

def listar_tablas_postgres_catalogo(request):
	
	db = psycopg2.connect(user='postgres', dbname='postgres', password='1234567', host='localhost')
	cursor = db.cursor()
	query = "select table_name from information_schema.tables"
	cursor.execute(query)
	tablas3 = [row[0] for row in cursor.fetchall()]
	dict = {'tablas3':tablas3}
	db.close()

	return HttpResponse(json.dumps(dict), content_type='application/json')

def listar_tablas_campos_postgres(request):
	dbs = request.POST.get('db')
	db = psycopg2.connect(user='postgres', dbname=dbs, password='1234567', host='localhost')
	cursor = db.cursor()
	value = request.POST.get('value')
	query = "select * from %s" %value
	cursor.execute(query)
	dict = {}
	for row in cursor:
		print row
		dict.setdefault(row[0],row[1:])
	print dict
	db.close()

	return HttpResponse(json.dumps(dict), content_type='application/json')

def listar_tablas_nombres_campos_postgres(request):
	dbs = request.POST.get('db')
	db = psycopg2.connect(user='postgres', dbname=dbs, password='1234567', host='localhost')
	cursor = db.cursor()
	value = request.POST.get('value')
	query = "select c.column_name FROM information_schema.columns c LEFT JOIN information_schema.element_types e ON c.table_catalog = e.object_catalog AND c.table_schema = e.object_schema AND c.table_name = e.object_name AND '%s' = e.object_type WHERE UPPER(c.table_name) = upper( '%s' ) ORDER BY c.ordinal_position" % (value,value)
	cursor.execute(query)
	nombres_campos = [row[0] for row in cursor.fetchall()]
	dict = { 'nombres_campos' : nombres_campos }
	db.close()

	return HttpResponse(json.dumps(dict), content_type='application/json')
