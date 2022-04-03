#python环境依赖
## 依赖
- Python packages
- environment variables  
- files out of scope  

```python
import ray
runtime_env = {"working_dir": "/data/my_files",
               "pip": ["requests", "pendulum==2.1.2"]}
ray.init(runtime_env=runtime_env)
```

### demo1
```python
import ray
runtime_env = {"working_dir": '/Users/4paradigm/Desktop/hyperC/ocr/play'}
ray.init(address="ray://172.27.67.85:30607", 
         _redis_password='5241590000000000',runtime_env=runtime_env)    

class FileReader:
    def __init__(self):
        with open("sample.txt",'rb') as f:
            self.content=f.read()
    def get_content(self):
        return self.content

ActorFileReader=ray.remote(num_cpus=0)(FileReader)

actor=ActorFileReader.options().remote()
ray.get(actor.get_content.remote())

#output[7]: b'WWW\n'
```

### demo2
```python
runtime_env = {
    "conda": {
        "dependencies":
        ["toolz", "dill", "pip", {
            "pip": ["pendulum", "ray[serve]"]
        }]
    },
    "env_vars": {"TF_WARNINGS": "none"}
}

runtime_env = {"working_dir": "/data/my_files", 
               "pip": ["requests", "pendulum==2.1.2"]}


import fakermaker
runtime_env={"py_modules": [fakermaker]}

```

## 任务/actor 环境
You can specify different runtime environments per-actor or per-task
using .options() or the @ray.remote() decorator:

## image
```python
runtime_env={"container":
                 {"image": "anyscale/ray-ml:nightly-py38-cpu",
                  "worker_path": "/root/python/ray/workers/default_worker.py",
                  "run_options": ["--cap-drop SYS_ADMIN","--log-level=debug"]}}
```

## persistency
Garbage Collection.
Runtime environment resources on each node
(such as conda environments, pip packages, or downloaded working_dir 
or py_modules folders) will be removed when they are no longer referenced by any actor, task or job. 
To disable this (for example, for debugging purposes) set the environment variable 
RAY_runtime_env_skip_local_gc to 1 on each node in your cluster before starting Ray (e.g. with ray start).