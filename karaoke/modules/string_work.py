import json
import os


# deleting trash information from string
def del_str_trash(string: str):
    index = str.rfind(string, '(Караоке)')
    if index == -1:
        return os.path.splitext(string)[0]
    else:
        index = str.rfind(string, '(')
        str_return = string[0:index]
        return str(str_return)


def get_song_info(string: str):
    # delete trash info from string
    string = del_str_trash(string)

    index = str.find(string, ' - ')
    if index == -1:
        song_info = {'artist': 'string', 'song': ''}
    else:
        artist = string[0:index]
        song = string[index+3:]
        song_info = {'artist': artist, 'song': song}

    return song_info


def get_list_song_info(textfile: str):
    with open(textfile) as json_file:
        files_list = json.load(json_file)
    song_info = list()
    for string in files_list:
        song_info.append(get_song_info(string))
    return song_info


def get_list_songs_json(textfile: str):
    with open(textfile) as json_file:
        files_list = json.load(json_file)
    list_songs = list()
    for string in files_list:
        list_songs.append(del_str_trash(string))
    return list_songs


def get_list_songs_folder(dir_path: str):
    files_list = os.listdir(dir_path)
    list_songs = list()
    for string in files_list:
        list_songs.append(del_str_trash(string))
    return list_songs
