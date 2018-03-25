from django.shortcuts import render
from .models import Tarea
from .models import Usuario
from .forms import TareaForm
from django.shortcuts import redirect

def lista_tareas(request):
	tareas = Tarea.objects.all();
	return render(request,'todolstsite/lista_tareas.html',{'tareas':tareas})

def agregar_tarea(request):
	if request.method=="POST":
		form = TareaForm(request.POST)
		if form.is_valid():
			tarea = form.save(commit=False)
			tarea.usuario_id = 1
			tarea.save()
			return redirect('agregar_tarea')
	else:
		form = TareaForm()

	return render(request,'todolstsite/agregar_tarea.html',{'form':form})