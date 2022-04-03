# k8s部署
## image
docker.4pd.io/ray_tensorflow2:pipe-105-commit-aa96d082

## deployment
1. k8s定义ray cluster资源
k apply -f cluster_crd.yaml
CRD: CustomResourceDefinition
   
2. 安装Ray Operator，op作为deployment支点 部署ray cluster
有两中方式部署ray operator
1）k apply -f  namespaced.yaml -n prophet 
2）edit namespace in cluster-scoped file
k apply -f  cluster_scoped.yaml -n prophet
   
3. 部署raycluster文件
1）edit cpu limit in example_cluster.yaml
2）设置内存，gpu， work_num等资源
2） k apply -f ray_tf_cluster.yaml -n prophet  // to start up ray cluster

4. 查看日志是否启动
/tmp/ray/session_latest  
   
[Ray GitHub](https://github.com/ray-project/ray/tree/master/deploy/components/)
[Deploying without Helm](https://docs.ray.io/en/master/cluster/kubernetes-advanced.html#k8s-advanced)
[ray-operator](https://docs.ray.io/en/master/cluster/kubernetes.html#ray-operator) 