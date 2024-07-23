#### Artefato 5: Exemplos de políticas IAM para GCP que suportam a arquitetura de governança proposta.

### API Gateway:

```json
{
  "bindings": [
    {
      "role": "roles/run.invoker",
      "members": [
        "serviceAccount:gw-sa@my-project.iam.gserviceaccount.com"
      ]
    }
  ]
}
```

### Cloud Run:
```json
{
  "bindings": [
    {
      "role": "roles/run.invoker",
      "members": [
        "serviceAccount:api-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/composer.user",
      "members": [
        "serviceAccount:api-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/dataproc.admin",
      "members": [
        "serviceAccount:api-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/iam.serviceAccountTokenCreator",
      "members": [
        "serviceAccount:api-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/bigquery.user",
      "members": [
        "serviceAccount:api-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/bigquery.jobUser",
      "members": [
        "serviceAccount:api-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/iam.serviceAccountUser", //permissao para anexar uma conta de serviço a um recurso.
      "members": [
        "serviceAccount:api-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/dataflow.admin",
      "members": [
        "serviceAccount:api-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/pubsub.Editor ",
      "members": [
        "serviceAccount:api-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/storage.objectUser",
      "members": [
        "serviceAccount:api-sa@my-project.iam.gserviceaccount.com"
      ]
    }
  ]
}


```
### DataFlow:
```json
{
  "bindings": [
    {
      "role": "roles/storage.objectUser",
      "members": [
        "serviceAccount:dataflow-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/pubsub.editor",
      "members": [
        "serviceAccount:dataflow-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/bigquery.dataEditor",
      "members": [
        "serviceAccount:dataflow-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/bigquery.user",
      "members": [
        "serviceAccount:dataflow-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/dataflow.worker",
      "members": [
        "serviceAccount:dataflow-sa@my-project.iam.gserviceaccount.com"
      ]
    },
  ]
}


```
### DataProc:
```json
{
  "bindings": [
    {
      "role": "roles/storage.objectUser",
      "members": [
        "serviceAccount:dataproc-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/bigquery.dataEditor",
      "members": [
        "serviceAccount:dataproc-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/bigquery.user",
      "members": [
        "serviceAccount:dataproc-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/dataproc.worker",
      "members": [
        "serviceAccount:dataproc-sa@my-project.iam.gserviceaccount.com"
      ]
    },
  ]
}


```
### Composer:
```json
{
  "bindings": [
    {
      "role": "roles/storage.objectUser",
      "members": [
        "serviceAccount:airflow-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/dataproc.admin",
      "members": [
        "serviceAccount:airflow-sa@my-project.iam.gserviceaccount.com"
      ]
    },
    {
      "role": "roles/composer.worker",
      "members": [
        "serviceAccount:airflow-sa@my-project.iam.gserviceaccount.com"
      ]
    },
  ]
}
```


verificar pq permissao de service account