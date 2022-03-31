# k8s部署
## deployment
1. k8s定义ray cluster资源
k apply -f RayCluster CRD 
CRD: CustomResourceDefinition
   
2. 安装Ray Operator，op作为deployment支点 部署ray cluster
有两中方式部署ray operator
1）k apply -f  namespaced -n prophet 
2）edit namespace in cluster-scoped file
   k apply -f  cluster-scoped -n prophet
   
3. 部署raycluster文件
1）edit cpu limit in example_cluster.yaml
2）设置内存，gpu， work_num等资源
2） k apply -f example_cluster.yaml -n prophet  // to start up ray cluster

[Ray GitHub](https://github.com/ray-project/ray/tree/master/deploy/components/)
[Deploying without Helm](https://docs.ray.io/en/master/cluster/kubernetes-advanced.html#k8s-advanced)
[ray-operator](https://docs.ray.io/en/master/cluster/kubernetes.html#ray-operator) 