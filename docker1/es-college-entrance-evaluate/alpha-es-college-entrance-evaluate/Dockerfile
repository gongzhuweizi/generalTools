FROM registry-vpc.cn-beijing.aliyuncs.com/wx-k8s-dev-alpha-beta/jdk1.8.0_252:v0
MAINTAINER wx
RUN rm -f /etc/localtime && ln -sv /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone
COPY es-college-entrance-evaluate.jar    /home/wx/services/es-college-entrance-evaluate/es-college-entrance-evaluate.jar
WORKDIR /home/wx/services/es-college-entrance-evaluate
#RUN mkdir -p   /home/wx/services/es-college-entrance-evaluate/logs 
ENTRYPOINT ["java","-Duser.timezone=Asia/Shanghai","-server","-Xms512m","-Xmx512m","-Xmn128m","-XX:MetaspaceSize=256m","-XX:MaxMetaspaceSize=256m","-XX:+HeapDumpOnOutOfMemoryError","-XX:HeapDumpPath=/home/wx/services/es-college-entrance-evaluate/logs/heapdump.hprof","-XX:+PrintGCDateStamps","-XX:+PrintGCDetails","-XX:+UseParallelGC","-XX:+UseParallelOldGC","-jar","es-college-entrance-evaluate.jar","--spring.cloud.nacos.config.server-addr=10.1.1.116:8848","--spring.cloud.nacos.discovery.server-addr=10.1.1.116:8848","--spring.profiles.active=alpha"]
