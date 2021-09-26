# Multi Thread Python

Pythonでマルチスレッドを扱う。

- [Multi Thread Python](#multi-thread-python)
  - [実行](#実行)
    - [準備](#準備)
    - [シングルスレッド](#シングルスレッド)
    - [マルチスレッド1](#マルチスレッド1)
    - [ThreadPoolExecutor](#threadpoolexecutor)
    - [Future](#future)
  - [参考](#参考)

## 実行

### 準備

```
docker-compose build
```

### シングルスレッド

``` sh
docker-compose run python single_thread
```

### マルチスレッド1

``` sh
docker-compose run python multi_thread_1
```


### ThreadPoolExecutor

``` sh
docker-compose run python thread_pool_executor
```

### Future

Threadから実行結果を取得する。

``` sh
docker-compose run python future
```

## 参考

- [\[Python\] スレッドで実装する:Qiita](https://qiita.com/tchnkmr/items/b05f321fa315bbce4f77)