import os
from mutagen.mp4 import MP4, MP4Cover

def embed_lrc_to_m4a():
    # 获取当前目录下的所有文件
    files = os.listdir(".")
    lrc_files = {os.path.splitext(f)[0]: f for f in files if f.endswith(".lrc")}
    m4a_files = {os.path.splitext(f)[0]: f for f in files if f.endswith(".m4a")}

    for song_name, lrc_file in lrc_files.items():
        if song_name in m4a_files:
            m4a_file = m4a_files[song_name]
            print(f"正在将歌词文件 {lrc_file} 嵌入到音频文件 {m4a_file} 中...")
            
            try:
                # 读取歌词文件内容
                with open(lrc_file, "r", encoding="utf-8") as f:
                    lyrics = f.read()
                
                # 加载 m4a 文件
                audio = MP4(m4a_file)
                
                # 将歌词嵌入到 m4a 文件
                audio["©lyr"] = lyrics
                
                # 保存更改
                audio.save()
                print(f"成功将 {lrc_file} 嵌入到 {m4a_file}！")
            except Exception as e:
                print(f"嵌入失败: {e}")
        else:
            print(f"未找到匹配的 m4a 文件: {song_name}.m4a")

if __name__ == "__main__":
    embed_lrc_to_m4a()
