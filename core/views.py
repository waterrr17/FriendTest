from django.shortcuts import render, redirect
from .models import Player

# Create your views here.
def test_start(request):
    ranking=Player.objects.order_by('-score')
    return render(request, 'core/test_start.html',{'ranking':ranking})

def test_end(request, currentPlayer):
    ranking=Player.objects.order_by('-score')
    # return render(request, 'core/test_end.html',{'ranking': ranking,})
    return render(request, 'core/test_end.html',{'ranking': ranking, 'currentPlayer': currentPlayer})

choices_set = [
    ['짜장면', '짬뽕'],
    ['부먹', '찍먹'],
    ['산', '바다'],
    ['민초', '레샤'],
    ['김치찌개', '된장찌개'],
    ['여름', '겨울'],
    ['연상', '연하'],
    ['비냉', '물냉'],
    ['개', '고양이'],
    ['콜라', '사이다'],
]


def guess(request):
    id = request.POST['friend_code']

    host = Player.objects.get(player_number=id)

    #첫 문제를 풀 때
    if host.current_guess == 0:
        player_number = Player.objects.count()+1
        name = request.POST['name']
        player = Player.objects.create(is_host=False, name=name, player_number=player_number)

    #첫 문제를 푸는 것이 아닐 때
    else:
        player_number = Player.objects.count()
        player = Player.objects.get(player_number=player_number)
        _guess = bool(int(request.POST['choice']))

        if host.current_guess == 1:
            answer = host.question1
            player.question1 = _guess
        elif host.current_guess == 2:
            answer = host.question2
            player.question2 = _guess
        elif host.current_guess == 3:
            answer = host.question3
            player.question3 = _guess
        elif host.current_guess == 4:
            answer = host.question4
            player.question4 = _guess
        elif host.current_guess == 5:
            answer = host.question5
            player.question5 = _guess
        elif host.current_guess == 6:
            answer = host.question6
            player.question6 = _guess
        elif host.current_guess == 7:
            answer = host.question7
            player.question7 = _guess
        elif host.current_guess == 8:
            answer = host.question8
            player.question8 = _guess
        elif host.current_guess == 9:
            answer = host.question9
            player.question9 = _guess
        elif host.current_guess == 10:
            answer = host.question10
            player.question10 = _guess

        if _guess == answer:
            player.score += 1
        player.save()

    if host.current_guess == 10:
        host.current_guess=0
        return redirect('test_end', currentPlayer=player)

    choices = choices_set[host.current_guess]
    host.current_guess+=1
    host.save()

    return render(request, 'core/guess.html', {
        'host': host,
        'player': player,
        'choice1': choices[0],
        'choice2': choices[1],
    })