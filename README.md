# Group1_MiniProject_2_SourceCode

## Team Division

| Team Member | Main Tasks | Technical Implementation |
| --- | --- | --- |
| Qingyuan You | S3 storage management and core MapReduce implementation for Output1 & Output2 | Create an Amazon S3 bucket and upload the dataset; use Amazon EMR or Hadoop Docker to implement the first two MapReduce tasks: sensor event count and building warning/error statistics. |
| Muhan Cai | Ray framework deployment and Task3 anomaly detection logic | Set up a Ray environment on AWS EC2 (single-node or simple cluster); write a parallel program using `@ray.remote` to detect anomalous devices (low battery, repeated errors, high temperature); ensure final anomaly list is merged through Ray's distributed execution. |
| Jintong Liu | MapReduce sorting for Output3 and performance comparison analysis | Implement the third MapReduce task: Top 10 most active devices (involving complex sorting/multi-stage processing); assist members A/B with system integration to ensure smooth AWS operation. |