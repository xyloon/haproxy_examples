## Two docker instances

* The first one is recevies http request from haproxy ,  prints out the request and response
* The other one is filter out web request based on the haproxy configuration

## Curl test


### GET

```
curl http://127.0.0.1:8080/abcdefg?abc=d
```


### POST
```
curl -X POST -H "User-Agent: linux bla bla" -H "Content-Type: application/json" \
-d " \
{ \
 \"path\":\"./directory/a.png\" }\
" \
http://127.0.0.1:8080/abcdefg
```