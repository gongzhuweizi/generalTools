FROM registry-vpc.cn-beijing.aliyuncs.com/wx-k8s-dev-alpha-beta/jdk1.8.0_252:v0
MAINTAINER wx
RUN rm -f /etc/localtime && ln -sv /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone
COPY es-api-gateway.jar    /home/wx/services/es-api-gateway/es-api-gateway.jar
WORKDIR /home/wx/services/es-api-gateway
#RUN mkdir -p   /home/wx/services/es-api-gateway/logs 
ENTRYPOINT ["java","-Duser.timezone=Asia/Shanghai","-server","-Xms512m","-Xmx512m","-Xmn128m","-XX:MetaspaceSize=256m","-XX:MaxMetaspaceSize=256m","-XX:+HeapDumpOnOutOfMemoryError","-XX:HeapDumpPath=/home/wx/services/es-api-gateway/logs/heapdump.hprof","-XX:+PrintGCDateStamps","-XX:+PrintGCDetails","-XX:+UseParallelGC","-XX:+UseParallelOldGC","-jar","es-api-gateway.jar","--spring.cloud.nacos.config.server-addr=10.1.1.119:8848","--spring.cloud.nacos.discovery.server-addr=10.1.1.119:8848","--spring.profiles.active=dev"]
