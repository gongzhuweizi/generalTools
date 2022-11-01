FROM registry-vpc.cn-beijing.aliyuncs.com/wx-k8s-dev-alpha-beta/jdk1.8.0_252:v0
MAINTAINER wx
RUN rm -f /etc/localtime && ln -sv /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone
COPY es-transaction-manager.jar    /home/wx/services/es-transaction-manager/es-transaction-manager.jar
WORKDIR /home/wx/services/es-transaction-manager
#RUN mkdir -p   /home/wx/services/es-transaction-manager/logs 
ENTRYPOINT ["java","-jar","es-transaction-manager.jar","-Duser.timezone=Asia/Shanghai","-server","-Xms512m","-Xmx512m","-Xmn128m","-XX:MetaspaceSize=128m","-XX:MaxMetaspaceSize=256m","-XX:+HeapDumpOnOutOfMemoryError","-XX:+PrintGCDateStamps","-XX:+PrintGCDetails","-XX:+UseParallelGC","-XX:+UseParallelOldGC","--spring.cloud.nacos.config.server-addr=10.1.1.116:8848","--spring.cloud.nacos.discovery.server-addr=10.1.1.116:8848","--spring.profiles.active=alpha"]
