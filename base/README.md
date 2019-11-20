# python-flask-pratice

## Base:
練習基本的 flask，並用 Bootstrap 4.1 製作頁面
[Bootstrap 4.1 文檔](https://getbootstrap.com/)

## Bootstrap
Bootstrap is an open source toolkit for developing with HTML, CSS, and JS. Quickly prototype your ideas or build your entire app with our Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful plugins built on jQuery.

## How to use

### Python
- 創建虛擬環境：`virtualenv venv`
- 運行 `python app.py`，訪問 [127.0.0.1:5000](127.0.0.1:5000)
- 如果想要方便debug：`export FLASK_ENV=development`

### Docker
- `docker build -t python-docker-dev .`
- `docker run --rm -it -d -p 9000:5000 python-docker-dev`
- 訪問 [127.0.0.1:9000](127.0.0.1:9000)


## Docker
- [Docker](https://docs.docker.com/)
- 打包成鏡像：
    - `docker build -t python-docker-dev .`
- 查看鏡像：
    - `docker images`
- 運行鏡像(-d: 後台運行)：
    - `docker run --rm -it -d -p 9000:5000 python-docker-dev`

- 查看 Docker 運行中的容器：
    - `docker ps -a`
- 停止運行中的容器：
    - `docker stop <container ID>`
