
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, BlogPostForm, YouTubeLinkForm
from .models import BlogPost
from youtube_transcript_api import YouTubeTranscriptApi
from django.contrib import messages
from django.http import JsonResponse
from youtube_transcript_api import YouTubeTranscriptApi

def redirect_to_login(request):
    return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()  
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    if request.method == 'POST':
        link_form = YouTubeLinkForm(request.POST)
        post_form = BlogPostForm(request.POST)
        if link_form.is_valid():
            youtube_link = link_form.cleaned_data['youtube_link']
            video_id = youtube_link.split('v=')[-1]
            try:
                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                content = ' '.join([entry['text'] for entry in transcript])
                post_form = BlogPostForm(initial={'content': content})
                if post_form.is_valid():
                    post = post_form.save(commit=False)
                    post.user = request.user
                    post.save()
                    messages.success(request, 'Blog post created successfully!')
                    return redirect('dashboard')
            except Exception as e:
                messages.error(request, f'Error fetching transcript: {e}')
        else:
            messages.error(request, 'Invalid YouTube link.')

    else:
        link_form = YouTubeLinkForm()
        post_form = BlogPostForm()

    return render(request, 'dashboard.html', {'link_form': link_form, 'post_form': post_form})

@login_required
def generate_content(request):
    if request.method == 'POST':
        youtube_link = request.POST.get('youtube_link')
        video_id = youtube_link.split('v=')[-1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        content = ' '.join([entry['text'] for entry in transcript])
        return JsonResponse({'content': content})
    return JsonResponse({'error': 'Invalid request'}, status=400)