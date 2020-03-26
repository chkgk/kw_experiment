from django.shortcuts import render, redirect
from kwtask.models import Player
from otree.models import Session

# custom wristband setup page
def process_payment(request, session_code):
    # get the current session by session_code
    sessions = Session.objects.filter(code=session_code)

    Players = Player.objects.filter()

    return