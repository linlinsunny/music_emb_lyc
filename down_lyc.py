import os
import requests
importeyed3
from mutagen.flac import FLAC

def get_lyrics_from_netease(title, artist):
    """
    从网易云音乐获取LRC歌词
    """
    # 构建请求URL
    url = f"http://music.163.com/api/song/lyric?id={artist}&lv=1&kv=1&tv=-1"
    headers = {'Referer': 'http://music.163.com/'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('lrc', {}).get('lyric', '')
    return ''

def embed_lyrics_to_mp3(mp3_file, lyrics):
    """
    将LRC歌词嵌入到MP3文件中
    """
    audio = eyed3.load(mp3_file)
    audio.tag.lyrics.set(lyrics)
    audio.tag.save()

def embed_lyrics_to_flac(flac_file, lyrics):
    """
    将LRC歌词嵌入到FLAC文件中
    """
    audio = FLAC(flac_file)
    audio.tags['USLT'] = lyrics
    audio.save()

def main():
    # 搜索当前目录下的所有MP3和FLAC文件
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.mp3') or file.endswith('.flac'):
                audio_file_path = os.path.join(root, file)
                try:
                    # 尝试提取音频文件的标题和艺术家信息
                    if file.endswith('.mp3'):
                        audio = eyed3.load(audio_file_path)
                        title = audio.tag.title or ''
                        artist = audio.tag.artist or ''
                    elif file.endswith('.flac'):
                        audio = FLAC(audio_file_path)
                        title = audio['title'][0] or ''
                        artist = audio['artist'][0] or ''
                    
                    # 从网易云音乐获取LRC歌词
                    lyrics = get_lyrics_from_netease(title, artist)
                    if lyrics:
                        # 嵌入LRC歌词到音频文件
                        if file.endswith('.mp3'):
                            embed_lyrics_to_mp3(audio_file_path, lyrics)
                        elif file.endswith('.flac'):
                            embed_lyrics_to_flac(audio_file_path, lyrics)
                        print(f"Lyrics embedded successfully in {audio_file_path}")
                    else:
                        print(f"No lyrics found for {audio_file_path}")
                except Exception as e:
                    print(f"Error processing {audio_file_path}: {e}")

if __name__ == "__main__":
    main()
