# Macau 701X Bus Route Tracker

面向课堂展示的 HTML 巴士报站演示。双击 `index.html` 即可查看；站点排成一条直线、三辆模拟巴士每3秒移动一个站，点击站点查看模拟剩余站数和ETA。

**注意：巴士位置、车辆数量、到站ETA为模拟数据，并非实时GPS。** `stops.json` 是整理好的公开路线快照，并不代表爬虫运行成功；`scraper.py` 是待实际验证的课堂示例，可能需要根据网页结构修改解析逻辑。

数据参考来源：https://motransportinfo.com/cn/route/701X/0 。正式演示前应核实全部站点名称、顺序和最新运营信息。

运行爬虫：

```bash
pip install -r requirements.txt
python scraper.py
```

若解析失败，将报错且不覆盖已有JSON。通过本地HTTP服务器运行网页可以读取JSON：

```bash
python -m http.server 8000
```

随后打开 http://localhost:8000 。如果直接双击HTML，使用内置快照。
