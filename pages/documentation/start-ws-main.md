<!--
.. title: Main启动WS
.. slug: start-ws-main
-->

```java
Bootstrap bootstrap = Bootstrap.builder()
                .websocketPort(8999)
                .isWebsocket(true)
                .websocketPath("/")
                .build()
                .start().block();
```
