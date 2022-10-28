from django.shortcuts import render
from django.views.generic import ListView, DetailView

from . models import VideoContent

# Create your views here.

class VideoContents(ListView):

    template_name = 'contents/index.html'
    context_object_name = 'videos'
    ordering = '-uploaded'
    model = VideoContent

    # def get_queryset(self):
    #     return VideoContent.objects.all()


class SpecificVideoContent(DetailView):

    template_name = 'contents/playVideo.html'
    context_object_name = 'video_stream'
    model = VideoContent

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        '''
        Here, "kwargs" is just: {'object': <Activity: Activity 2>} but
        self.kwargs if dictonary of keyword agruments "<int: pk>" --> {'pk': 12}
        '''
        context['videos'] = VideoContent.objects.exclude(pk=self.kwargs['pk']).order_by('-uploaded')
        return context



     
