# 下载ECharts到本地以提高加载速度

## 方法1：手动下载（推荐）

### 步骤1：创建lib目录
在项目根目录下创建一个`lib`文件夹：
```
项目根目录/
├── lib/           # 新建这个文件夹
├── data/
├── index.html
└── ...
```

### 步骤2：下载文件
访问以下链接并下载文件到`lib`目录：

1. **ECharts主文件**：
   - 访问：https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js
   - 右键 → 另存为 → 保存到 `lib/echarts.min.js`

2. **PapaParse文件**：
   - 访问：https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js
   - 右键 → 另存为 → 保存到 `lib/papaparse.min.js`

### 步骤3：修改index.html
将index.html的第7-9行改为：
```html
<script src="lib/echarts.min.js"></script>
<script src="lib/papaparse.min.js"></script>
```

## 方法2：使用命令行下载（Windows）

在项目根目录打开命令行，执行：

```cmd
mkdir lib
curl -o lib/echarts.min.js https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js
curl -o lib/papaparse.min.js https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js
```

如果没有curl，可以使用PowerShell：
```powershell
New-Item -ItemType Directory -Force -Path lib
Invoke-WebRequest -Uri "https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js" -OutFile "lib/echarts.min.js"
Invoke-WebRequest -Uri "https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js" -OutFile "lib/papaparse.min.js"
```

## 方法3：使用Python下载

创建一个`download_libs.py`文件：

```python
import urllib.request
import os

# 创建lib目录
os.makedirs('lib', exist_ok=True)

# 下载文件
files = {
    'lib/echarts.min.js': 'https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js',
    'lib/papaparse.min.js': 'https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js'
}

for filename, url in files.items():
    print(f'正在下载 {filename}...')
    urllib.request.urlretrieve(url, filename)
    print(f'✓ {filename} 下载完成')

print('\n所有文件下载完成！')
print('请修改index.html中的script标签指向本地文件。')
```

然后运行：
```bash
python download_libs.py
```

## 完成后的目录结构

```
项目根目录/
├── lib/
│   ├── echarts.min.js      # ECharts库
│   └── papaparse.min.js    # PapaParse库
├── data/
│   └── CGED-Q Public Release 1760-1798  1 Jul 2024.tab
├── index.html
├── README.md
└── ...
```

## 优点

1. **加载速度更快**：不依赖外部CDN
2. **离线可用**：无需网络连接
3. **稳定性更好**：不受CDN服务影响

## 注意事项

- 地图数据仍然需要从阿里云DataV加载（需要网络连接）
- 如果需要完全离线，可以下载地图GeoJSON文件到本地