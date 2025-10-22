#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
将Stata .dta文件转换为制表符分隔的.tab文件
用于在网页中加载CGED-Q数据
"""

import sys
import os

try:
    import pandas as pd
    print("✓ pandas库已安装")
except ImportError:
    print("❌ 错误：需要安装pandas库")
    print("请运行: pip install pandas")
    sys.exit(1)

def convert_dta_to_tab(dta_file, tab_file=None):
    """
    将.dta文件转换为.tab文件
    
    参数:
        dta_file: 输入的.dta文件路径
        tab_file: 输出的.tab文件路径（可选，默认为同名.tab文件）
    """
    # 检查输入文件是否存在
    if not os.path.exists(dta_file):
        print(f"❌ 错误：文件不存在: {dta_file}")
        return False
    
    # 如果没有指定输出文件，使用同名.tab文件
    if tab_file is None:
        tab_file = os.path.splitext(dta_file)[0] + '.tab'
    
    try:
        print(f"\n开始转换...")
        print(f"输入文件: {dta_file}")
        print(f"输出文件: {tab_file}")
        print("\n正在读取.dta文件...")
        
        # 读取.dta文件
        df = pd.read_stata(dta_file)
        
        print(f"✓ 成功读取 {len(df)} 条记录，{len(df.columns)} 个字段")
        print(f"\n字段列表:")
        for i, col in enumerate(df.columns, 1):
            print(f"  {i}. {col}")
        
        print(f"\n正在写入.tab文件...")
        
        # 保存为制表符分隔的文件
        df.to_csv(tab_file, sep='\t', index=False, encoding='utf-8')
        
        print(f"✓ 转换成功！")
        print(f"\n输出文件: {tab_file}")
        print(f"文件大小: {os.path.getsize(tab_file) / 1024 / 1024:.2f} MB")
        
        return True
        
    except Exception as e:
        print(f"❌ 转换失败: {str(e)}")
        return False

def main():
    print("=" * 60)
    print("CGED-Q Stata数据转换工具")
    print("将.dta文件转换为网页可用的.tab格式")
    print("=" * 60)
    
    # 默认文件路径
    default_file = "data/CGED-Q Public Release 1760-1798  1 Jul 2024.dta"
    
    if len(sys.argv) > 1:
        dta_file = sys.argv[1]
    else:
        dta_file = default_file
        print(f"\n使用默认文件: {dta_file}")
        print("(您也可以指定文件: python convert_dta_to_tab.py <文件路径>)")
    
    # 执行转换
    success = convert_dta_to_tab(dta_file)
    
    if success:
        print("\n" + "=" * 60)
        print("✓ 转换完成！现在可以在浏览器中打开 index.html")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ 转换失败，请检查错误信息")
        print("=" * 60)
        sys.exit(1)

if __name__ == "__main__":
    main()