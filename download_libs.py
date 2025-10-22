#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
下载ECharts和PapaParse库到本地
运行此脚本后，需要手动修改index.html中的script标签
"""

import urllib.request
import os
import sys

def download_file(url, filename):
    """下载文件"""
    try:
        print(f'正在下载 {filename}...')
        urllib.request.urlretrieve(url, filename)
        file_size = os.path.getsize(filename) / 1024  # KB
        print(f'✓ {filename} 下载完成 ({file_size:.1f} KB)')
        return True
    except Exception as e:
        print(f'✗ {filename} 下载失败: {e}')
        return False

def main():
    print('=' * 60)
    print('ECharts和PapaParse库下载工具')
    print('=' * 60)
    print()
    
    # 创建lib目录
    lib_dir = 'lib'
    if not os.path.exists(lib_dir):
        os.makedirs(lib_dir)
        print(f'✓ 创建目录: {lib_dir}/')
    else:
        print(f'✓ 目录已存在: {lib_dir}/')
    print()
    
    # 要下载的文件
    files = {
        'lib/echarts.min.js': 'https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js',
        'lib/papaparse.min.js': 'https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js'
    }
    
    # 下载文件
    success_count = 0
    for filename, url in files.items():
        if download_file(url, filename):
            success_count += 1
        print()
    
    # 显示结果
    print('=' * 60)
    if success_count == len(files):
        print(f'✓ 所有文件下载完成！({success_count}/{len(files)})')
        print()
        print('下一步：修改index.html')
        print('-' * 60)
        print('将index.html的第7-9行改为：')
        print()
        print('  <script src="lib/echarts.min.js"></script>')
        print('  <script src="lib/papaparse.min.js"></script>')
        print()
        print('然后删除或注释掉原来的CDN链接。')
    else:
        print(f'✗ 部分文件下载失败 ({success_count}/{len(files)})')
        print('请检查网络连接后重试。')
    print('=' * 60)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n下载已取消。')
        sys.exit(1)
    except Exception as e:
        print(f'\n\n发生错误: {e}')
        sys.exit(1)