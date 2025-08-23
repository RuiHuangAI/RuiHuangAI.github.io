#!/usr/bin/env python3
from PIL import Image
import os

def generate_favicon():
    # 打开原始图片
    try:
        img = Image.open('images/RuiHuang.png')
        
        # 生成不同尺寸的favicon
        sizes = {
            'favicon-16x16.png': (16, 16),
            'favicon-32x32.png': (32, 32),
            'apple-touch-icon.png': (180, 180),
            'android-chrome-192x192.png': (192, 192),
            'android-chrome-512x512.png': (512, 512)
        }
        
        for filename, size in sizes.items():
            # 调整图片大小，保持比例
            resized_img = img.resize(size, Image.Resampling.LANCZOS)
            
            # 如果是小尺寸，创建圆形图标
            if size[0] <= 32:
                # 创建圆形遮罩
                mask = Image.new('L', size, 0)
                # 这里可以添加圆形处理，但为了简单，我们直接保存方形
                resized_img.save(f'images/{filename}')
            else:
                resized_img.save(f'images/{filename}')
            
            print(f"✅ 生成 {filename}")
        
        # 生成ICO文件（Windows favicon）
        img_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
        img_32.save('images/favicon.ico', format='ICO')
        print("✅ 生成 favicon.ico")
        
        print("\n所有favicon文件已生成完成！")
        
    except Exception as e:
        print(f"❌ 错误: {e}")

if __name__ == "__main__":
    generate_favicon() 