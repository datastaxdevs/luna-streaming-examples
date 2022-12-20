# tag::helm-repo-add[]
helm repo add datastax-pulsar https://datastax.github.io/pulsar-helm-chart
# end:helm-repo-add[]

# tag::helm-install[]
helm install \
  --namespace datastax-pulsar \
  --create-namespace \
  --values ${VALUES_URL} \
  --version 3.0.4 \
  my-pulsar-cluster \
  datastax-pulsar/pulsar
# end:helm-install[]

# tag::wait-for-broker[]
kubectl -n datastax-pulsar wait --for=condition=Ready pod/pulsar-broker-0
# end::wait-for-broker[]