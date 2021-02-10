from django.views import generic
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404

# Create your views here.
'''def  home (request): 
    
    return render(request,'blogindex.html') '''

class PostList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'blogindex.html'

'''class PostDetail(generic.DetailView):
    model= Post
    template_name = 'blogpost_detail.html'
'''

# I will be modifying post_detail as shown below

def post_detail(request, slug):
    template_name = 'blogpost_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True) #retreive all approved comments of a post 
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST) #the comment_form attribute holds the data of user input
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # (Assign the current post to the comment) 
            # Since comment has a field named post, we are retrieving the post of new_comment and assigning it to post
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
