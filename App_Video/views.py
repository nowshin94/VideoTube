from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from App_Video.models import Category, Video, Comment, Likes
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Video.forms import CommentForm
import uuid

# Create your views here.

def search(request):
    if request.method == "GET":
        search = request.GET.get('search', '')
        result = Category.objects.all().filter(title__icontains=search)
    return render(request, 'App_Video/vid_search.html', context={'search':search,'result':result})

class MyVideos(LoginRequiredMixin, TemplateView):
    template_name = 'App_Video/my_videos.html'

class CreateVideo(LoginRequiredMixin, CreateView):
    model = Video
    template_name = 'App_Video/create_video.html'
    fields = ('video_title', 'video_image',)

    def form_valid(self, form):
        video_obj = form.save(commit=False)
        video_obj.author = self.request.user
        title = video_obj.video_title
        video_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        video_obj.save()
        return HttpResponseRedirect(reverse('index'))

class CategoryList(ListView):
    model = Video
    template_name = 'App_Video/video_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context

@login_required
def video_details(request, slug):
    video = Video.objects.get(slug=slug)
    comment_form = CommentForm()
    already_liked = Likes.objects.filter(video=video, user= request.user)
    if already_liked:
        liked = True
    else:
        liked = False
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.video = video
            comment.save()
            return HttpResponseRedirect(reverse('App_Video:video_details', kwargs={'slug':slug}))
    return render(request, 'App_Video/video_details.html', context={'video':video, 'comment_form':comment_form, 'liked':liked,})

@login_required
def liked(request, pk):
    video = Video.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(video=video, user=user)
    if not already_liked:
        liked_video = Likes(video=video, user=user)
        liked_video.save()
    return HttpResponseRedirect(reverse('App_Video:video_details', kwargs={'slug':video.slug}))

@login_required
def unliked(request, pk):
    video = Video.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(video=video, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Video:video_details', kwargs={'slug':video.slug}))

class UpdateVideo(LoginRequiredMixin, UpdateView):
    model = Video
    fields = ('video_title', 'video_image')
    template_name = 'App_Video/edit_video.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('App_Video:video_details', kwargs={'slug':self.object.slug})



