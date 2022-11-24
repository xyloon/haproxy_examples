## HAProxy branching with domain name

### Test steps

* apply test domain in /etc/hosts
* run `webserver #1`
* run `webserver #2`
* `docker-compose -f docker-compose-domain-split.yaml up`
