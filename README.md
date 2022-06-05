# tele-mnist

## SetUP

Set up secret

```sh
kubectl create secret generic tel-secret\
    --from-literal=tel_token=xxxYOURTOKENxxx\
    --from-literal=admin_ID=xxxYOURTELEGRAMIDxxx
```
