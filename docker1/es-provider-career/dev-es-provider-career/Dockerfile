FROM registry-vpc.cn-beijing.aliyuncs.com/wx-k8s-dev-alpha-beta/jdk1.8.0_252:v0
MAINTAINER wx
RUN rm -f /etc/localtime && ln -sv /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone && mkdir -p /tmp/gc_logs/ 
COPY inotify_rsync.sh    /home/wx/services/es-provider-career/inotify_rsync.sh
COPY es-provider-career.jar    /home/wx/services/es-provider-career/es-provider-career.jar
WORKDIR /home/wx/services/es-provider-career
#RUN mkdir -p   /home/wx/services/es-provider-career/logs 
ENTRYPOINT ["java","-Duser.timezone=Asia/Shanghai","-server","-Xms1024m","-Xmx1024m","-Xmn256m","-XX:MetaspaceSize=256m","-XX:MaxMetaspaceSize=256m","-XX:+HeapDumpOnOutOfMemoryError","-XX:HeapDumpPath=/home/wx/services/es-provider-career/logs/heapdump.hprof","-XX:+PrintGCDateStamps","-XX:+PrintGCDetails","-Xloggc:/tmp/gc_logs/gc.log","-XX:+UseParallelGC","-XX:+UseParallelOldGC","-jar","es-provider-career.jar","--spring.cloud.nacos.config.server-addr=10.1.1.119:8848","--spring.cloud.nacos.discovery.server-addr=10.1.1.119:8848","--spring.profiles.active=dev"]
