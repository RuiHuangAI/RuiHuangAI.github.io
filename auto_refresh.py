#!/usr/bin/env python3
import os
import time
import subprocess
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class JekyllHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified = 0
        self.debounce_time = 0.8  # 2秒防抖
        
    def on_modified(self, event):
        if event.is_directory:
            return
            
        current_time = time.time()
        if current_time - self.last_modified > self.debounce_time:
            self.last_modified = current_time
            print(f"\n检测到文件变化: {event.src_path}")
            self.rebuild_site()
    
    def rebuild_site(self):
        try:
            print("正在重新构建网站...")
            result = subprocess.run(['bundle', 'exec', 'jekyll', 'build'], 
                                  capture_output=True, text=True, cwd='.')
            if result.returncode == 0:
                print("✅ 网站构建成功！")
            else:
                print(f"❌ 构建失败: {result.stderr}")
        except Exception as e:
            print(f"❌ 构建错误: {e}")

def start_http_server():
    """启动HTTP服务器"""
    try:
        print("启动HTTP服务器在端口4000...")
        subprocess.run(['python3', '-m', 'http.server', '4000'], cwd='_site')
    except KeyboardInterrupt:
        print("\n服务器已停止")

def main():
    # 首先构建一次
    print("初始构建网站...")
    subprocess.run(['bundle', 'exec', 'jekyll', 'build'])
    
    # 启动文件监控
    event_handler = JekyllHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    
    print("开始监控文件变化...")
    print("访问 http://localhost:4000 查看网站")
    print("按 Ctrl+C 停止")
    
    # 在后台启动HTTP服务器
    server_thread = threading.Thread(target=start_http_server, daemon=True)
    server_thread.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n停止监控...")
    
    observer.join()

if __name__ == "__main__":
    main() 