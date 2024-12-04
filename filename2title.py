import os
import eyed3

def update_mp3_title():
    # 获取当前工作目录
    directory = os.getcwd()
    
    # 遍历当前目录下的所有文件
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):  # 确保是MP3文件
            filepath = os.path.join(directory, filename)
            try:
                audiofile = eyed3.load(filepath)
                
                # 获取文件名（不含后缀）
                title = os.path.splitext(filename)[0]
                
                # 更新ID3标签中的Title字段
                audiofile.tag.title = title
                audiofile.tag.save()  # 保存更改
                print(f"Updated title for: {filename}")
            except Exception as e:
                print(f"Failed to update {filename}: {e}")

# 调用函数
update_mp3_title()
