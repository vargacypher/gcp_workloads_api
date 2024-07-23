## Endpoints:
- **/v1/healthcheck**- Checar status da API
- **/v1/workloads/batch-cluster/submit-demo**  - Submeter workload spark para contar palavras
- **/v1/workloads/batch-cluster/get-demo-status/{workload_id}** - Resgatar status do Dataproc job
- **/v1/workloads/batch-cluster/get-demo-result**  - Retorna 100 registros da tabela que armaneza a contagem final do job spark.

### Teste na API

```shell

#Exporta a URL do servico cloud run
export URL=$(gcloud run services describe workloads-api --format='value(status.url)')
#Seleciona a regiao
32 us-central1 OU SUA $REGIAO

export STS_TOKEN=$(gcloud auth print-identity-token)

curl $URL/healthcheck -H "Authorization: Bearer $STS_TOKEN"

curl -X 'POST' $URL/v1/workloads/batch-cluster/submit-demo?python_file_url=gs%3A%2F%2Ftest_spk%2Fspark_word_count.py -H "Authorization: Bearer $STS_TOKEN"

#Utilizar o workload_id retornado no step anterior para resgatar o status
curl $URL/v1/workloads/batch-cluster/get-demo-status/$WORKLOAD_ID_RETORNADO_NO_CURL_ANTERIOR -H "Authorization: Bearer $STS_TOKEN"  

curl $URL/v1/workloads/batch-cluster/get-demo-result -H "Authorization: Bearer $STS_TOKEN"
```