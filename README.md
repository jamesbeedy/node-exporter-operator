# Prometheus Node Exporter Charm

Prometheus [node exporter](https://github.com/prometheus/node_exporter) for
machine metrics.

## Quickstart

Deploy the `prometheus-node-exporter` charm and relate it to the units you want
to export the metrics:

```bash
$ juju deploy prometheus-node-exporter
$ juju integrate prometheus-node-exporter foo
```

## License

The charm is maintained under the Apache v2 license. See `LICENSE` file in this
directory for full preamble.

Copyright &copy; 2025 Vantage Compute Corporation
