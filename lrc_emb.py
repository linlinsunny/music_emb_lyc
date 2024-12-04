import os
import eyed3
from mutagen.flac import FLAC, Picture

def embed_lrc_to_mp3(mp3_file, lrc_content):
    """
    将LRC歌词嵌入到MP3文件中
    """
    audio = eyed3.load(mp3_file)
    audio.tag.lyrics.set(lrc_content)
    audio.tag.save()

def embed_lrc_to_flac(flac_file, lrc_content):
    """
    将LRC歌词嵌入到FLAC文件中
    """
    audio = FLAC(flac_file)
    # 直接向tags字典添加歌词
    audio.tags['USLT'] = lrc_content
    audio.save()

def embed_lrc_to_audio(audio_file, lrc_content):
    """
    根据文件类型将LRC歌词嵌入到音频文件中
    """
    if audio_file.endswith('.mp3'):
        embed_lrc_to_mp3(audio_file, lrc_content)
    elif audio_file.endswith('.flac'):
        embed_lrc_to_flac(audio_file, lrc_content)

def find_and_embed_lrc():
    """
    搜索当前目录下的所有MP3和FLAC文件，并将相应的LRC文件嵌入
    """
    # 搜索当前目录下的所有MP3和FLAC文件
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.mp3') or file.endswith('.flac'):
                audio_file_path = os.path.join(root, file)
                # 构造LRC文件名
                lrc_file_name = file.rsplit('.', 1)[0] + '.lrc'
                lrc_file_path = os.path.join(root, lrc_file_name)
                
                # 检查LRC文件是否存在
                if os.path.exists(lrc_file_path):
                    with open(lrc_file_path, 'r', encoding='utf-8') as lrc_file:
                        lrc_content = lrc_file.read()
                    embed_lrc_to_audio(audio_file_path, lrc_content)
                    print(f"LRC embedded successfully in {audio_file_path}")
                else:
                    print(f"LRC file not found for {audio_file_path}")

if __name__ == "__main__":
    find_and_embed_lrc()
