from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Poll
from django.http import HttpResponse
# Create your views here.
@login_required
def vote(request):
    poll=Poll.objects.get(pk=1)
    if request.method=='POST':
        selected_option=request.POST['poll']
        if selected_option=="option1":
            poll.option_one_count+=1
        elif selected_option=="option2":
            poll.option_two_count+=1
        elif selected_option=="option3":
            poll.option_three_count+=1
        elif selected_option=="option4":
            poll.option_four_count+=1
        elif selected_option=="option5":
            poll.option_five_count+=1
        elif selected_option=="option6":
            poll.option_six_count+=1
        else:
            return HttpResponse(400,'invalid form go back')
        poll.save()
        return redirect('vote:results')

    context={'poll':poll}
    return render(request,'vote.html',context)

def results(request):
    poll=Poll.objects.get(pk=1)
    context={'poll':poll}
    return render(request,'results.html',context)
