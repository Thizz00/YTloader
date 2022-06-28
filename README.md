# YT-Downloader

`pip install PyQt5`
`pip install pytube`

```python
from pytube import YouTube
yt = YouTube(link)
yt.streams.get_highest_resolution().download(path)
```


![alt text](obraz_2022-01-05_163702.png)
