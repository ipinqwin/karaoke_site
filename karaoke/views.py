from django.http import HttpResponse
from django.template import loader
import json
import os
import karaoke.modules.string_work
import karaoke.settings
import pathlib as Path


def index(request):
    # html page to view
    template = loader.get_template('index.html')

    # load video list from file
    pathfile = '/var/www/www-root/data/site_songs_list/karaoke/static/list_videos.txt'
    with open(pathfile) as json_file:
        video_list = json.load(json_file)

    # context transfer to html
    context = {
        'video_list': video_list
    }

    return HttpResponse(template.render(context))


def update_list(request):
    print('Function not work')
    ## html page to view
    # template = loader.get_template('update.html')
    #
    # # load video list from directory
    # list_dir = os.listdir(karaoke.settings.DIR_VIDEOS)
    # # delete trash info from files
    # list_songs = list()
    # for string in list_dir:
    #     list_songs.append(karaoke.modules.string_work.del_str_trash(string))
    #
    # # save to the file
    # with open(str(karaoke.settings.BASE_DIR) + '\\karaoke\\static\\list_videos.txt', 'w') as json_file:
    #     json.dump(list_songs, json_file)
    #
    # return HttpResponse(template.render())
