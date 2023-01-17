# <font color='orchid'><center> Local __Airflow Instance__ </center></font>
<center>A local airflow instance deployed with the official airflow helm chart in a minikube cluster</center>

<br>

### <font color='limegreen'> __components__ </font> 

* __airflow-namespace.yml__: creates the namespace in which we will deploy ou airflow instance
* __airflow-variables-configmap.yml__: creates variables to be deployed within our airflow instance

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