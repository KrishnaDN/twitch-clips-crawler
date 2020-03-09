import re
import urllib.request
import requests
import sys
import os

base_clip_path = 'https://clips-media-assets2.twitch.tv/'
clip_txt_file=sys.argv[1]
cid = sys.argv[2]
basepath ='/mnt/archive/Twitch_clips/downloads/'+clip_txt_file.split('/')[-1][:-4]
if not os.path.exists(basepath):
    os.makedirs(basepath)
def retrieve_mp4_data(slug):
    clip_info = requests.get(
        "https://api.twitch.tv/helix/clips?id=" + slug,
        headers={"Client-ID": cid}).json()
    thumb_url = clip_info['data'][0]['thumbnail_url']
    title = clip_info['data'][0]['title']
    slice_point = thumb_url.index("-preview-")
    mp4_url = thumb_url[:slice_point] + '.mp4'
    return mp4_url, title


def dl_progress(count, block_size, total_size):
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%" % percent)
    sys.stdout.flush()


# for each clip in clips.txt
for clip in open(clip_txt_file, 'r'):
    slug = clip.split('/')[3].replace('\n', '')
    mp4_url, clip_title = retrieve_mp4_data(slug)
    regex = re.compile('[^a-zA-Z0-9_]')
    clip_title = clip_title.replace(' ', '_')
    out_filename = regex.sub('', clip_title) + '.mp4'
    output_path =basepath +'/'+ out_filename
    print(output_path)
    print('\nDownloading clip slug: ' + slug)
    print('"' + clip_title + '" -> ' + out_filename)
    print(mp4_url)
    try:
        urllib.request.urlretrieve(mp4_url, output_path, reporthook=dl_progress)
    except:
        continue
    print('\nDone.')

print('Finished downloading all the videos.')
