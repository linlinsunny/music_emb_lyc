#!/bin/bash

# 搜索当前目录及其子目录中的所有 .lrc 文件
find . -type f -name '*.lrc' -print0 | while IFS= read -r -d '' file; do
    # 移动文件到废纸篓
    mv "$file" ~/.Trash/
done