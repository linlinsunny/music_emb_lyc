import os
import subprocess

def convert_flac_to_m4a():
    # 获取当前目录下的所有 .flac 文件
    flac_files = [f for f in os.listdir(".") if f.endswith(".flac")]
    
    if not flac_files:
        print("当前文件夹中没有找到任何 FLAC 文件。")
        return
    
    # 创建输出文件夹
    output_folder = "converted_m4a"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for flac_file in flac_files:
        # 构造输出文件路径
        base_name = os.path.splitext(flac_file)[0]
        m4a_file = os.path.join(output_folder, f"{base_name}.m4a")
        
        print(f"正在转换: {flac_file} -> {m4a_file}")
        try:
            # 使用 ffmpeg 转换 FLAC 到 M4A (ALAC)，明确指定流
            subprocess.run(
                [
                    "ffmpeg",
                    "-i", flac_file,  # 输入文件
                    "-vn",            # 禁用视频流
                    "-c:a", "alac",   # 使用 ALAC 编码
                    m4a_file          # 输出文件
                ],
                check=True
            )
            print(f"转换完成: {m4a_file}")
        except subprocess.CalledProcessError as e:
            print(f"转换失败: {flac_file}, 错误: {e}")
    
    print(f"所有 FLAC 文件已转换完成，输出目录: {output_folder}")

if __name__ == "__main__":
    convert_flac_to_m4a()
