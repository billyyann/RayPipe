## 简介
Easy implementation and abstraction for train and deploy model on ray cluster

## 资源清单
1. docker image  
   docker.4pd.io/ray_tensorflow2:pipe-105-commit-aa96d082
2. 安装文档  
./doc
3. 安装
pip install raypip
   
## Feature
- 提供FastAPi 异步接口，支持mysql， 支持crud方法
- 基于K8s, Ray cluster 实现远程训练，部署
- 基于装饰器实现高度抽象，模型实现build_model_func, generate_date_func可以通过代理方式远程训练部署
- 提供基于FS，In memory(开发中)， Ray Sync(开发中) 等单节点，分布式存储
- 基于装饰器实现配置类，类似@Bean效果，在运行中决定生成实现类
