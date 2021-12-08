<!--
.. title: 版本
.. slug: release
.. date: 2021-09-20 18:21:38 UTC+1
.. tags: tag
.. category: category
.. link: link
.. description:
.. type: text
-->


## RELEASE版本
- [gitee](https://gitee.com/quickmsg/mqtt-cluster/releases)
- [github](https://github.com/quickmsg/smqtt/releases)


## 发布清单

### 1.1.0

> - 新增grafana监控，支持influxdb，prometheusd数据源
> - 修复已知集群bug

### 1.0.9

>新增系统事件类型
> - 设备离线事件
> - 设备在线事件

### 1.0.8

> - 优化项目启动配置类，支持yaml,properties
> - 支持更多配置类参数
> - 优化拦截器
> - 优化集群路由
> - 认证接口添加clientIdentifier
> - 新增规则引擎，规则引擎支持Jexl3表达式
> - 支持配置常用的外部数据源source
> - 支持springboot启动starter
> - 支持系统流控
> - 修复了极端情况bytebuf释放异常
