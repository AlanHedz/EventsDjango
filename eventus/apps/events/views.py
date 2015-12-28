from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from .models import Event, Category, Comments
from .forms import EventForm, CommentsForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.models import User
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin

# Create your views here.

#def index(request):
#	events = Event.objects.all().order_by('		-created')[:6]
#	categories = Category.objects.all()
#	return render(request, 'events/index.html', {'events': events, 'categories':categories})
class IndexView(TemplateView):
	template_name = 'events/index.html'
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['events'] = Event.objects.all().order_by('-created')[:6]
		context['categories'] = Category.objects.all()
		return context


#def main_panel(request):
#	events = Event.objects.filter(organizer__username='AlanHedz').order_by('is_free', '-created')
#	cantidad_eventos = events.count()
#	return render(request,'events/panel/panel.html', {'events': events, 'cantidad': cantidad_eventos})
class MainPanelView(LoginRequiredMixin, TemplateView):
	login_url = 'users_app:login'
	template_name = 'events/panel/panel.html'
	def get_context_data(self, **kwargs):
		context = super(MainPanelView, self).get_context_data(**kwargs)
		context['events'] = Event.objects.filter(organizer = self.request.user).order_by('is_free', '-created')
		context['cantidad'] = context['events'].count()
		return context

#def crear_evento(request):
#	if request.method == 'POST':
#		modelform = EventForm(request.POST, request.FILES)
#		if modelform.is_valid():
#			organizador = User.objects.get(pk="1")
#			nuevo_evento = modelform.save()
#			nuevo_evento.organizer = organizador
#			nuevo_evento.save()
#			return redirect(reverse('events_app:panel'))
#	else:
#		modelform = EventForm()
#
#	return render(request, 'events/panel/crear_evento.html', {'form': modelform})
class CreateEvent(LoginRequiredMixin, CreateView):
	login_url = 'users_app:login'
	form_class = EventForm
	template_name = "events/panel/crear_evento.html"
	success_url = reverse_lazy('events_app:panel')

	def form_valid(self,form):
		form.instance.organizer = self.request.user
		return super(CreateEvent, self).form_valid(form)


#def detalle_evento(request, evento_id):
#	event = get_object_or_404(Event, pk=evento_id)
#	return render(request, 'events/panel/detalle_evento.html',{'event': event})
class EventDetail(DetailView):
	template_name = "events/panel/detalle_evento.html"
	model = Event

#def editar_evento(request, evento_id):
#	event = get_object_or_404(Event, pk=evento_id)
#
#	if request.method == 'POST':
#		modelform = EventForm(request.POST, request.FILES, instance=event)
#		if modelform.is_valid():
#			modelform.save()
#			return redirect(reverse('events_app:panel'))
#	else:
#		modelform = EventForm(instance=event)
#
#	return render(request, 'events/panel/editar_evento.html', {'form': modelform, 'event': event})
class EventEdit(LoginRequiredMixin, UpdateView):
	login_url = 'users_app:login'
	template_name = 'events/panel/editar_evento.html'
	model = Event
	form_class = EventForm
	success_url = reverse_lazy('events_app:panel')

	def form_valid(self,form):
		form.instance.organizer = self.request.user
		return super(EventEdit, self).form_valid(form)

#def eliminar_evento(request, evento_id):
#	event = get_object_or_404(Event, pk=evento_id)
#
#	if request.method == 'POST':
#		event.delete()
#		return redirect(reverse('events_app:panel'))
#
#	return render(request, 'events/panel/eliminar_evento.html', {'event': event})
class EventDelete(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
	login_url = 'users_app:login'
	template_name = 'events/panel/eliminar_evento.html'
	model = Event
	succes_url = reverse_lazy('events_app:panel')
	context_object_name = 'event'

def create_comment(request):
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		modelform = CommentsForm(request.POST)
		if modelform.is_valid():
			nuevo_comentario = modelform.save()
			nuevo_comentario.user = self.request.user
			nuevo_comentario.event = post
			return redirect(reverse('events_app:detalle'))
	else:
		modelform = CommentsForm()

	return render(request, 'events/panel/detalle_evento.html', {'form': modelform})