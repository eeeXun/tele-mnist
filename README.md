# tele-mnist

## SetUP

Set up secret

```sh
kubectl create secret generic tel-secret --from-literal=tel_token=xxxYOURTOKENxxx
```

Set up all service

```sh
kubectl apply -f deploy/
```
