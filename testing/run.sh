#!/bin/sh

k6 run --out influxdb=http://localhost:8086/mnist script.js
