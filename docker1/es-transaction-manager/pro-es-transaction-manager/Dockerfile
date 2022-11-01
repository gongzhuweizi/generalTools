FROM registry-vpc.cn-beijing.aliyuncs.com/wx-k8s-dev-alpha-beta/jdk1.8.0_252:v0
MAINTAINER wx
RUN rm -f /etc/localtime && ln -sv /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone
#COPY es-transaction-manager.jar    /home/wx/services/es-transaction-manager/es-transaction-manager.jar
COPY es-transaction-manager.jar    /home/wx/services/es-transaction-manager/es-transaction-manager.jar
WORKDIR /home/wx/services/es-transaction-manager
#ENTRYPOINT ["java","-jar","es-transaction-manager.jar","-Duser.timezone=Asia/Shanghai","-server","-Xms2g","-Xmx2g","-Xmn512m","-XX:MetaspaceSize=256m","-XX:MaxMetaspaceSize=512m","-XX:+HeapDumpOnOutOfMemoryError","-XX:+PrintGCDateStamps","-XX:+PrintGCDetails","-XX:+UseParallelGC","-XX:+UseParallelOldGC","--spring.cloud.nacos.config.server-addr=10.0.0.189:8848","--spring.cloud.nacos.discovery.server-addr=10.0.0.189:8848","--spring.profiles.active=pro"]

#apply skywalking config template start service
ENTRYPOINT ["java","-javaagent:/home/wx/apache-skywalking-apm-bin-es7/agent/skywalking-agent.jar","-Dskywalking_config=/home/wx/apache-skywalking-apm-bin-es7/agent/config/es-transaction-manager.config","-jar","es-transaction-manager.jar","-Duser.timezone=Asia/Shanghai","-server","-Xms2g","-Xmx2g","-Xmn512m","-XX:MetaspaceSize=256m","-XX:MaxMetaspaceSize=512m","-XX:+HeapDumpOnOutOfMemoryError","-XX:+PrintGCDateStamps","-XX:+PrintGCDetails","-XX:+UseParallelGC","-XX:+UseParallelOldGC","--spring.cloud.nacos.config.server-addr=10.0.0.189:8848","--spring.cloud.nacos.discovery.server-addr=10.0.0.189:8848","--spring.profiles.active=pro"]
