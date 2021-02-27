# aea fetchai

https://docs.fetch.ai/aea/quickstart/

```
pipenv install 'aea[all]'
```

```
pipenv shell
aea init
```

```
(fetchai_aea_agent) ➜  fetchai_aea_agent git:(develop) ✗ aea init
Please enter the author handle you would like to use: hiroshi 
Do you have a Registry account? [y/N]: 
Create a new account on the Registry now:
Email: 
Password: 
Please make sure that passwords are equal.
Confirm password: 
Do you want to subscribe for developer news? [y/N]: y
Please visit `https://aea-registry.fetch.ai/mailing-list` to subscribe for developer news
Successfully registered and logged in: hiroshi
    _     _____     _    
   / \   | ____|   / \   
  / _ \  |  _|    / _ \  
 / ___ \ | |___  / ___ \ 
/_/   \_\|_____|/_/   \_\
                         
v0.10.1

AEA configurations successfully initialized: {'author': 'hiroshi'}
(fetchai_aea_agent) ➜  fetchai_aea_agent git:(develop) ✗ 
```

### Echo skill

```
aea create aea_agent
cd aea_agent
aea add skill fetchai/echo:0.14.0
```

```
aea add connection fetchai/http_server:0.16.0
```

```
aea run
```