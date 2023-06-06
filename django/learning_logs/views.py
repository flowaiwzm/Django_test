import csv
import json
from django.core.files.storage import FileSystemStorage
import requests
import matplotlib.pyplot as plt
from http.client import HTTPResponse
import uuid
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Topic
from .forms import TopicForm, EntryForm, MyForm
from .models import Topic, Entry, MyModel
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from random import sample
import os
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
from collections import Counter
import matplotlib
matplotlib.use('Agg')  # 使用agg模式


def index(request):
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    selected_fruits = sample(fruits, 1)

    res1=github_api(request)#'res1':res1,,'res2':res2
    # res2=visualization(request)
    # res3=weather_predict(request)
    return render(request, 'learning_logs/index.html', {'fruits': selected_fruits,'res1':res1})


@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Show a single topic, and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect(('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    # if topic.owner != request.user:
    #     raise Http404

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


@login_required
def delete_topic(request, topic_id):
    # 获取要删除的模型实例
    topic = Topic.objects.get(id=topic_id)
    topic.delete()
    # 返回删除结果
    return redirect(reverse('learning_logs:topics'))  # 重定向到指定页面


@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES:
        myfile = request.FILES['myfile']
        file_contents = myfile.read().decode('utf-8')
        fs = FileSystemStorage()
        ext = myfile.name.split('.')[-1]
        filename = '{}.{}'.format(str(uuid.uuid4()), ext)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'hidden_url_field': uploaded_file_url,
            'file_contents': file_contents,
        })
    return render(request, 'upload.html')


# @login_required
def github_api(request):
    # 在此处填写你的 GitHub API key
    api_key = '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'

    # 发送 HTTP 请求，获取 GitHub 用户信息
    response = requests.get(
        'https://api.github.com/user', auth=('token', api_key))
    user_info = response.json()
    # print(user_info)
    # 渲染模板并将用户信息传递给模板
    return user_info
@login_required
def weather_predict(request):
    api_key = "911b7c71486eea869fda20bcc8098902"  # 替换为你自己的API Key
    city = request.GET.get('city')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # 将 JSON 数据转换为 Python 字典
        # # 提取温度信息
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        wind_deg = data['wind']['deg']
        cloudiness = data['clouds']['all']
        temps = [temp_min, temp, temp_max]
        fig, axs = plt.subplots(2, 3, figsize=(15, 9))
        fig.suptitle('Weather Information for Changsha, China')

        # 温度
        axs[0, 0].bar(['Temperature'], [temp], color='red')
        axs[0, 0].set_title('Temperature')
        axs[0, 0].set_ylabel('Degrees Celsius')
        axs[0, 0].text(0, temp+0.1, f'{temp}°C', ha='center', va='bottom')


        # 湿度
        axs[0, 1].bar(['Humidity'], [humidity], color='blue')
        axs[0, 1].set_title('Humidity')
        axs[0, 1].set_ylabel('Percentage')
        axs[0, 1].text(0, humidity+0.5, f'{humidity}%', ha='center', va='bottom')

        # 气压
        axs[0, 2].bar(['Pressure'], [pressure], color='green')
        axs[0, 2].set_title('Pressure')
        axs[0, 2].set_ylabel('hPa')
        axs[0, 2].text(0, pressure+1, f'{pressure}hPa', ha='center', va='bottom')

        # 风速
        axs[1, 0].bar(['Wind Speed'], [wind_speed], color='orange')
        axs[1, 0].set_title('Wind Speed')
        axs[1, 0].set_ylabel('m/s')
        axs[1, 0].text(0, wind_speed, f'{wind_speed}m/s', ha='center', va='bottom')

        # 风向
        axs[1, 1].pie([wind_deg, 360-wind_deg], labels=['Wind Direction', ''], colors=['black', 'green'])
        axs[1, 1].set_title('Wind Direction')
        axs[1, 1].text(0, 0, f'{wind_deg}°', ha='center', va='center')

        # 云量
        axs[1, 2].bar(['Cloudiness'], [cloudiness], color='gray')
        axs[1, 2].set_title('Cloudiness')
        axs[1, 2].set_ylabel('Percentage')
        axs[1, 2].text(0, cloudiness, f'{cloudiness}%', ha='center', va='bottom')
        buffer = io.BytesIO()
        canvas = FigureCanvas(fig)
        canvas.print_png(buffer)
        img = base64.b64encode(buffer.getvalue()).decode('utf-8')
        context = {'img': img}
        return render(request, 'weather.html', {'data':data,'context':context})
    else:
        print("Error fetching data from OpenWeatherMap API")
    

@login_required
def visualization(request):
    file_path = os.path.join(
        settings.BASE_DIR, 'learning_logs\static\learning_logs\cosmetics.csv')
    with open(file_path, 'r',encoding='MacRoman') as f:
        # 读取CSV文件的代码
        reader = csv.reader(f)
        header_row = next(reader)
        #获取功效列表
        fun=header_row[6:]
        #初始化各样本数量，平均价格，平均排名，价格，类型，品牌，排名，有功效的次数，无功效的次数
        num=[0,0,0,0,0,0]
        price_avg=[0,0,0,0,0,0]
        rank_avg=[0,0,0,0,0,0]
        prices=[]
        labels=[]
        brands=[]
        ranks=[]
        fun_s=[0,0,0,0,0]
        fun_f=[0,0,0,0,0]
        for row in reader:
            price=float(row[3])
            rank=float(row[4])
            label=str(row[0])
            brand=str(row[1])
            ranks.append(rank)
            brands.append(brand)
            labels.append(label)
            prices.append(price)
            labels=list(dict.fromkeys(labels))
            if str(row[0])=='Moisturizer':
                num[0]+=1
                price_avg[0]+=price
                rank_avg[0]+=rank
            elif str(row[0])=='Cleanser':
                num[1]+=1
                price_avg[1]+=price
                rank_avg[1]+=rank
            elif str(row[0])=='Treatment':
                num[2]+=1
                price_avg[2]+=price
                rank_avg[2]+=rank
            elif str(row[0])=='Face Mask':
                num[3]+=1
                price_avg[3]+=price
                rank_avg[3]+=rank
            elif str(row[0])=='Eye cream':
                num[4]+=1
                price_avg[4]+=price
                rank_avg[4]+=rank
            else:
                num[5]+=1
                price_avg[5]+=price
                rank_avg[5]+=rank
            if float(row[6])==1:
                fun_s[0]+=1
            else:
                fun_f[0]+=1
            if float(row[7])==1:
                fun_s[1]+=1
            else:
                fun_f[1]+=1
            if float(row[8])==1:
                fun_s[2]+=1
            else:
                fun_f[2]+=1
            if float(row[9])==1:
                fun_s[3]+=1
            else:
                fun_f[3]+=1
            if float(row[10])==1:
                fun_s[4]+=1
            else:
                fun_f[4]+=1
    for i in range(6):
        price_avg[i]=round(price_avg[i]/num[i],2)
        rank_avg[i]=round(rank_avg[i]/num[i],4)
    brands=Counter(brands)
    brand_names = list(brands.keys())
    brand_counts = list(brands.values())
    # # 绘制柱形图
    fig, ax = plt.subplots(nrows=3,ncols=2,figsize=(16,14))
    colors = ['r', 'g', 'b', 'y', 'm','black']
    ax[0][0].pie(num,labels=labels,autopct='%1.1f%%')
    ax[0][0].set_title("Proportion Pie Chart of Sample Varieties")
    ax[0][1].bar(labels,price_avg,color=colors)
    for i in range(len(labels)):
        ax[0][1].text(labels[i], price_avg[i] + 0.5, price_avg[i], ha='center')
    ax[0][1].set_title("Price bar chart of sampled product categories")
    ax[1][0].bar(brand_names,brand_counts)
    ax[1][0].set_title("Bar chart of sample quantity for each brand")
    ax[1][1].bar(labels,rank_avg)
    ax[1][1].set_title("Bar chart of average ranking of samples")
    for i in range(len(labels)):
        ax[1][1].text(labels[i], rank_avg[i], rank_avg[i], ha='center')

    ax[2][0].bar(x=fun,height=fun_s,label='success',color='green',alpha=0.8)
    ax[2][0].bar(x=fun,height=fun_f,label='success',color='pink',alpha=0.8)
    for x, y in enumerate(fun_s):
        ax[2][0].text(x, y-2, '%s' % y, ha='center', va='bottom')
    for x, y in enumerate(fun_f):
        ax[2][0].text(x, y-2 , '%s' % y, ha='center', va='bottom')
    ax[2][0].set_title("Component analysis bar chart ")
    ax[2][1].plot(labels,price_avg)
    for i in range(len(labels)):
        ax[2][1].text(labels[i], price_avg[i] + 0.5, price_avg[i], ha='center')
    ax[2][1].set_title("Price line chart of sampled product categories")
    # # 添加图表标题和坐标轴标签
    # # 将图表数据渲染到HTML模板中
    buffer = io.BytesIO()
    canvas = FigureCanvas(fig)
    canvas.print_png(buffer)
    data = base64.b64encode(buffer.getvalue()).decode('utf-8')
    context = {'data': data}
    return render(request, 'data.html',context)
