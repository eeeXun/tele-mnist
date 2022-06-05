# tele-mnist

## SetUP

Set up secret

```sh
kubectl create secret generic tel-secret\
    --from-literal=tel_token=xxxYOURTOKENxxx\
    --from-literal=admin_ID=xxxYOURTELEGRAMIDxxx
```

Set up all service

```sh
kubectl apply -f deploy/
```
## telbot
![圖片](https://user-images.githubusercontent.com/52521773/172043584-0a82e756-2c7b-4b87-8234-81c084eece5a.png)
### bot command
+ hi - say hi to the user
+ set_host - set new server set_host (Admin only)
+ feed_back - send a feed back so we can know which picture is wrong
+ (send pic) - return number in the pic

### How to use
1. scan the QRcode above
2. type the command above 
