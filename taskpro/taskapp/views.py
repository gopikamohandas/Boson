from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *
from .forms import *



@api_view()

def nav(request):
    return render (render,'nav.html')

def home(request):
    return render (request,'home.html')

# def main(request):
#     return render (request,'main.html')

class Task(APIView):
    def get(self, request):
        dict_task = {
            'objtodo' : Todo.objects.all()
        }
        serializer=TodoSerializer(dict_task, many=True)
        return render(request, 'main.html', dict_task)
class NewTask(APIView):  
    def get(self, request):
        form = TodoForm()
        dict_form = {
                'form':form
        }
        return render(request,'create.html', dict_form) 
    def post(self, request):
            form=TodoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('main')
            else:
                return render(request,'create.html',{'form':form})
            
def TaskUpdate(request,pk):
        task = Todo.objects.get(pk=pk)
        if request.method=='POST':
            form = TodoForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('main')
        form1= TodoForm(instance=task)
        dicti_form={
            'form':form1
        }
        return render(request, 'update.html', dicti_form)
            

def delete(request, pk):
        obj = Todo.objects.get(pk=pk)
        obj.delete()
        return redirect ('main')
    



    
