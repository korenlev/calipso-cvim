#!/usr/bin/env python3

"""
2017/01/12 11:05:39 added by Kun
kunch@cisco.com
This script is a simple example to decode data from kafka topic of sensor raw data.
"""

from kafka import KafkaConsumer
import avro.schema
import avro.io
import io

# To consume messages
consumer = KafkaConsumer('metrics',
                         group_id='osdna_test',
                         bootstrap_servers=['localhost:9092'])

schema_path = "metricRecord.avsc"
schema = avro.schema.Parse(open(schema_path).read())

for msg in consumer:
    bytes_reader = io.BytesIO(msg.value)
    decoder = avro.io.BinaryDecoder(bytes_reader)
    reader = avro.io.DatumReader(schema)
    record = reader.read(decoder)
    print(record)
