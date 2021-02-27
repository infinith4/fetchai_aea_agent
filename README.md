# aea fetchai

https://docs.fetch.ai/aea/quickstart/

https://aea-registry.fetch.ai/

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
aea add connection fetchai/stub:0.17.0
aea add protocol fetchai/default:0.12.0
```

```
aea add connection fetchai/http_server:0.16.0
```


```
aea run
```


other terminal

```
echo 'recipient_aea,sender_aea,fetchai/default:0.12.0,\x08\x01\x12\x011*\x07\n\x05hello,' >> input_file
```

```
aea interact
```

running above command in terminal

paste below command

```
echo 'recipient_aea,sender_aea,fetchai/default:0.12.0,\x08\x01\x12\x011*\x07\n\x05hello,' >> input_file
```

you can see

terminal of "aea run"

```
info: [aea_agent] Echo Behaviour: act method called.
info: [aea_agent] Echo Handler: message=Message(sender=aea_agent_interact,to=aea_agent,content=b"echo 'recipient_aea,sender_aea,fetchai/default:0.12.0,\x08\x01\x12\x011*\x07\n\x05hello,' >> input_file",dialogue_reference=('e1be93a7101d01683dfb323606b341c49b4138512ca406791eccfffbc9733b68', ''),message_id=1,performative=bytes,target=0), sender=aea_agent_interact
```

terminal of "aea interact"

```
Provide message of protocol 'fetchai/default:0.12.0' for performative bytes:
echo 'recipient_aea,sender_aea,fetchai/default:0.12.0,\x08\x01\x12\x011*\x07\n\x05hello,' >> input_file

Sending envelope:
to: aea_agent
sender: aea_agent_interact
protocol_specification_id: fetchai/default:0.1.0
message: Message(sender=aea_agent_interact,to=aea_agent,content=b"echo 'recipient_aea,sender_aea,fetchai/default:0.12.0,\x08\x01\x12\x011*\x07\n\x05hello,' >> input_file",dialogue_reference=('d138af525a4b4746c575a09adca234075e9b5df36ba9c510a4d8357718aa509c', ''),message_id=1,performative=bytes,target=0)
```