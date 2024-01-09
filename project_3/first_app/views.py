from django.shortcuts import render
import datetime
def home(request):
    data={'author': 'jahid','last_name':'hasan rahman','age':20, 'Roll' :1911018,'list':['Python','is','Best'], 'birthday': datetime.datetime.now() ,'courses':[
        { 'name':'cse',
        'id':1} ,
        { 'name':'mse',
        'id':2} ,
        { 'name':'bme',
        'id':3} ,
    ],
     'text_nmbr':'two',

     'lst':[
    {'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 22},
    {'name': 'Joe', 'age': 31},
]
       

    }


    return render(request,'first_app/home.html',data)

# Create your views here.
