from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from users.models import User
from cash.models import Money

from cash.forms import Transfer_money

# Create your views here.


def index(request):
    context = {'title': 'Банк'}
    return render(request, "cash/index.html", context)

def deposite(request):
    context = {'title':'Deposite'}
    return render(request, "cash/deposite.html", context)

def transfer(request):
    if request.method == 'POST':
        print("POST")
        form = Transfer_money(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks')
        
    else:
        form = Transfer_money()

    context = {'title':'Transfer', 'form': form}

    return render(request, 'cash/transfer.html', context)



    # return render(request, "cash/transfer.html", context)

@login_required
def bank(request):
    username = request.user.cardg
    # post = Money.objects.filter(card=username).values().first()
    context = {'title':'Bank', 'card': username}
    return render(request, "cash/bank.html", context)

def transfer_money(request):
    if request.method == 'POST':
        print("POST")
        card_ = request.POST.get('cd')
        money_ = request.POST.get('mn')

        cardmyself = request.user.cardg
        # Money.objects.get(cardh=cardmyself).money
        cardmyself = Money.objects.get(cardh=cardmyself)
        cardsend = Money.objects.get(cardh=card_)

        cardmyself.money -= int(money_)
        cardsend.money += int(money_)

        cardmyself.save()
        cardsend.save()
        print("Succesful")

    # return HttpResponseRedirect('/')




    return HttpResponseRedirect(request.META['HTTP_REFERER'])