from django.urls import reverse_lazy
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
class AboutView(TemplateView):
    template_name = 'blog_app/about.html'


class PostListView(ListView):
    model = Post
    template_name = 'blog_app/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Post
    success_url = reverse_lazy('blog_app:post_list')


class DraftListView(LoginRequiredMixin, ListView):
    template_name = 'blog_app/post_draft_list.html'
    login_url = '/login/'
    redirect_field_name = 'post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-create_date')


##########
# Comments
##########

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # nazwa jest ustawiona w name= w pliku urls.py
            return redirect('blog_app:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog_app/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog_app:post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog_app:post_detail', pk=post_pk)


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog_app:post_detail', pk=pk)
