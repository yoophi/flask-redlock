# FlaskRedlock

RedLock(Distributed locks with Redis and Python) 라이브러리를 Flask에서 사용하기 편하게 만든 wrapper 입니다.

```python
from flask import Flask
from flask_redlock import FlaskRedLock

app = Flask(__name__)
redlock = FlaskRedLock(app)
# 또는 
# redlock = FlaskRedLock()
# redlock.init_app(app)

lock = redlock.create_lock("some_lock")
lock.acquire()
do_something()
lock.release()

# 또는
with redlock.create_lock("some_lock"):
    do_something()
```

redlock 에 대한 자세한 내용은 <https://github.com/glasslion/redlock> 를 참고하세요.