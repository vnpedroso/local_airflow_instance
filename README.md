# <font color='orchid'><center> __Local Airflow Instance__ </center></font>
<center>A local airflow instance deployed with the official airflow helm chart in a minikube cluster</center>

<br>

### <font color='limegreen'> __components__ </font> 

* __airflow-namespace.yml__: creates the namespace in which we will deploy ou airflow instance
* __airflow-variables-configmap.yml__: creates variables to be deployed within our airflow instance
* __airflow-values.yml__: main yaml config file to be used as a reference for the deployment of the helm chart
* __Dockerfile__: the dockerfile containing the customization of airflow base image used in the instance
* __/dags__: folder containing a sample dag to be built-in inside our airflow customized image definied in the Dockerfile

<br>

### <font color="limegreen"> __starting minikube cluster__ </font>
I'm using minikube in this example, but this might work with k3d, k3s, kind and any other container orchestration tool that runs locallys. To start your minikube cluster, run the following:
```shell
minikube start --memory=<MEMORY_SPECS> --cpus=<CPU_SPECS>
```
<br>

### <font color="limegreen"> __building customized image__</font>
From __lines 48 to 55__ of the __airflow-values.yml__ file we have the definitions of the image to be used in the deployment of the helm chart. The image tag and name defined there should match the tag and the image name that you will build and load into the minikube cluster. 
```shell
docker build -t airflow_extended_image:1.0 .
```

```shell
minikube load airflow_extended_image:1.0
```

<br>

### <font color="limegreen"> __installing airflow helm chart__ </font>
To install airflow official helm chart, run the following command:
```shell
helm repo add apache-airflow https://airflow.apache.org
```
Then deploy the airflow instance specifying the __airflow-values.yml__ as the reference for helm:
```shell
helm upgrade --install airflow apache-airflow/airflow -f ./airflow-values.yml -n airflow-namespace --debug 
```

<br>

### <font color='limegreen'> __checking variables created with airflow_variables_configmap.yml__ </font>
Variables created with the configmap will not be available with the webserver UI. However, they will be in your instance. You can check on them executing a terminal inside either the __webserver pod__ or the __scheduler pod__:

```shell
kubectl exec --stdin --tty <webserver_pod_name or scheduler_pod_name> -n <namespace_name> -- /bin/bash
```
Once inside the pod's terminal run the following to check on the variables: 

```shell
from airflow.models import Variable
Variable.get("<variable_name>")
```
<br>

### <font color="limegreen"> __enabling airflow webserver__ </font>
In the __line 984__ of __airflow-values.yml__ file, there is type of the service that the webserver will use to be available. If using minikube, you can set it to a __Loadbalancer__, and run the following in a dedicated terminal:
```shell
minikube tunell
```

If using __ClusterIP__ as service type, which is the default, run the following in a dedicated terminal:
```shell
kubectl port-forward -n airflow-namespace svc/airflow-webserver 8080:8080
```

The webserver will be available at your localhost at port 8080, access it through your browser at __http://127.0.0.1:8080__