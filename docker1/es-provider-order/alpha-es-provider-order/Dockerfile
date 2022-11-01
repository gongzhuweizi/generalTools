FROM registry-vpc.cn-beijing.aliyuncs.com/wx-k8s-dev-alpha-beta/jdk1.8.0_252:v0
MAINTAINER wx
RUN rm -f /etc/localtime && ln -sv /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone
COPY es-provider-order.jar    /home/wx/services/es-provider-order/es-provider-order.jar
WORKDIR /home/wx/services/es-provider-order
#RUN mkdir -p   /home/wx/services/es-provider-order/logs 
ENTRYPOINT ["java","-Duser.timezone=Asia/Shanghai","-server","-Xms512m","-Xmx512m","-Xmn128m","-XX:MetaspaceSize=256m","-XX:MaxMetaspaceSize=256m","-XX:+HeapDumpOnOutOfMemoryError","-XX:HeapDumpPath=/home/wx/services/es-provider-order/logs/heapdump.hprof","-XX:+PrintGCDateStamps","-XX:+PrintGCDetails","-XX:+UseParallelGC","-XX:+UseParallelOldGC","-jar","es-provider-order.jar","--spring.cloud.nacos.config.server-addr=10.1.1.116:8848","--spring.cloud.nacos.discovery.server-addr=10.1.1.116:8848","--spring.profiles.active=alpha"]
