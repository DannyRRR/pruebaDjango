from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$',views.lista_tareas),
	url(r'^agregar_tarea$',views.agregar_tarea,name="agregar_tarea"),
]