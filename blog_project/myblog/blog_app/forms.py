from django import forms
from blog_app.models import Post, Comment  #app_name.model 

class PostForm(forms.ModelForm):
    class Meta():
        model = Post #Connect the model we are using
        fields = ('author','title','text') #edit author,title,text
        
        #add css widgets and their classes
        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}) # this coming from medium text library
        } 

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
