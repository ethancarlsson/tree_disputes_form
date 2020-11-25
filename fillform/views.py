from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .highlight import Write1, Write2
from .models import Question, Choice


def index(request):
    if request.method == 'POST':
        ### these are the possible answers
        repre = ['No. I am representing myself.', 'Yes I will have a legal representative.', 'Yes I will have an agent representing me.', 'Yes I will have an authorised officer representing me.']
        owner = ['Yes, the owner lives on the property.', 'No, the owner lives somewhere else.']
        tree_hedge = ['It is a tree that could damage, has damaged or is damaging my property.', 'It is a tree that could injure someone.', 'It is a hedge that is obstructing sunlight to a window on my property.', 'It is a hedge that is obstructing a view from my property.']
        heritage = ['Yes', 'No']

        
        answers = request.POST

        post = str(request.POST)

        ## these form ids use the answers to link to the correct static word_document
        form_id = str(repre.index(answers['1'])) + str(owner.index(answers['2'])) + str(tree_hedge.index(answers['3'])) + str(heritage.index(answers['4']))
        form_id2 = str(tree_hedge.index(answers['3']))
        
        ## these are the static word docs that will be used

        formc = '/static/formfolder/Tree Dispute Application Form C Version 3' + form_id + '.docx'
        formg = '/static/formfolder/application_treedispute_claimdetails_highhedges' + form_id2 + '.docx'
        formh = '/static/formfolder/application_treedispute_damage_to_property' + form_id2 + '.docx'
        question_list = Question.objects.all()

        context = {'question_list': question_list, 'formc': formc,'formg': formg, 'formh': formh}
        if "It is a tree that could damage, has damaged or is damaging my property." in post:
            return render(request, 'fillform/Tree.html', context)
        elif "It is a tree that could injure someone." in post:
            return render(request, 'fillform/Tree.html', context)
        else:
            return render(request, 'fillform/Hedge.html', context)

    else:
        question_list = Question.objects.all()
        context = {'question_list': question_list}
        return render(request, 'fillform/index.html', context)


def ssl(request):
    return render(request, 'fillform/first.html')
def ssl2(request):
    return render(request, 'fillform/second.html')


def home(request):
    return render(request, 'fillform/home.html')
