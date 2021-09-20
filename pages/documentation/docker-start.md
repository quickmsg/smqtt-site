<!--
.. title: Docker启动
.. slug: docker-start
-->

## 拉取最新版本镜像

```bash
# 拉取docker镜像地址
docker pull 1ssqq1lxr/smqtt:latest
```
## 准备配置文件
   
`同上新建config.properties文件`

# 启动服务

```bash
docker run -it  -v <配置文件路径目录>:/conf -p <宿主机port>:<配置文件port>  1ssqq1lxr/smqtt
```