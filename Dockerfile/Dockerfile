FROM registry-vpc.cn-beijing.aliyuncs.com/wx-k8s-dev-alpha-beta/jdk1.8.0_252:v0
MAINTAINER wx
RUN rm -f /etc/localtime \
&& ln -sv /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "Asia/Shanghai" > /etc/timezone \
&& mkdir -p /tmp/gc_logs/
COPY inotify_rsync.sh    $serviceDeployDir/$serviceName/inotify_rsync.sh
COPY $serviceName.jar    $serviceDeployDir/$serviceName/$serviceName.jar
WORKDIR $serviceDeployDir/$serviceName
#RUN mkdir -p   $serviceDeployDir/$serviceName/logs
ENTRYPOINT ["java","-Duser.timezone=Asia/Shanghai","-server","-Xms$memXms","-Xmx$memXmx","-Xmn$memXmn","-XX:MetaspaceSize=$metaSpaceSize","-XX:MaxMetaspaceSize=$maxMetaSpaceSize","-XX:+HeapDumpOnOutOfMemoryError","-XX:HeapDumpPath=$serviceDeployDir/$serviceName/logs/heapdump.hprof","-XX:+PrintGCDateStamps","-XX:+PrintGCDetails","-Xloggc:/tmp/gc_logs/gc.log","-XX:+UseParallelGC","-XX:+UseParallelOldGC","-jar","$serviceName.jar","--spring.cloud.nacos.config.server-addr=$nacosAddress","--spring.cloud.nacos.discovery.server-addr=$nacosAddress","--jasypt.encryptor.password=$mysqlPasswdEncryptionInfo","--spring.profiles.active=$deploymentEnv"]

