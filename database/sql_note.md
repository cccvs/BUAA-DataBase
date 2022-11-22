#### PRE

* 如果数据库断开连接，需要在命令行`net start mysql`。
* 登录命令行[管理员身份]` mysql -u root -p`。

```sql
show databases;	# 显示所有数据库,'show schemas;'也可以
use <database_name>;	# 选中要使用的数据库
show tables;	# 显示当前数据库中所有的表
desc <table_name>;	# 查看表结构
```

#### 1119

* `Free Talk`项目没用使用`user`内容。

#### 1122

* 修改`root`密码。

```mysql
use mysql;
show tables;
ALTER user 'root' @ 'localhost' IDENTIFIED BY '123456';
```

* `python`连接`mysql`数据库，用`pycharm`下载安装包会连接超时。于是用浏览器去下载[连接器](https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.25/mysql-connector-java-8.0.25.jar)，参考[教程](https://blog.csdn.net/fan521dan/article/details/104902294)进行配置即可。
