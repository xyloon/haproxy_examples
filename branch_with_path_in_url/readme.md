## HAProxy branching with path ^/site2/

http://127.0.0.1:18080/site2/* --> site2
http://127.0.0.1:18080/*(the others) --> site1

### Test steps

* `docker-compose up -d`
* Check site A
    * curl http://127.0.0.1:18080/
    * curl http://127.0.0.1:18080/another.html
* Check site B
    * curl http://127.0.0.1:18080/site2/
    * curl http://127.0.0.1:18080/site2/another.html
