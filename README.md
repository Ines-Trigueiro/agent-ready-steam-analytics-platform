# agent-ready-steam-analytics-platform
An agent-ready Steam analytics platform (Dagster, dbt, BigQuery, dlt, Terraform) with a Kimball warehouse, asset checks and freshness monitoring, and a cost-guarded MCP server that lets Claude answer business questions from dbt documentation and lineage.


## Prerequisites
- [Helm](https://helm.sh/docs/intro/install/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [k9s](https://k9scli.io/topics/install/)

## Usage

```
helm dependency update k8s
helm upgrade --install platform k8s --create-namespace --namespace platform
```