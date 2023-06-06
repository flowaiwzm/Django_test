import subprocess
from django.shortcuts import render
import os
# Create your views here.
def alien_invasion(request):
    # base_file=os.path.dirname(os.path.abspath(__file__))
    subprocess.Popen(['python', './aliens_game/games/aliens/Alien-Game/src/alien_invasion.py']) # 启动游戏主程序
    return render(request, 'aliens_game/alien_invasion.html')

def index(request):
    return render(request,'aliens_game/index.html')