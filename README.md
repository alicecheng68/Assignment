要求三

mysql>insert into member(name,username,password)values("Alice","test","test");
mysql>insert into member(name,username,password,follower_count)values("Amy","amy","testamy",100);
mysql>insert into member(name,username,password,follower_count)values("Ines","ines","testines",666);
mysql>insert into member(name,username,password,follower_count)values("Peggy","peggy","testpeggy",888);
mysql>insert into member(name,username,password,follower_count)values("Annie","annie","testannie",168);

mysql>INSERT INTO member (id, name, username, password, follower_count, time)
-> VALUES (9, "Cynthia", "cynthia", "testcynthia", 678, '2023-07-31 22:59:59'),
-> (7, "Vivian", "vivian", "testvivian", 123, NOW()),
-> (6,"Katy","katy","testkaty",666,"2023-07-28 13:20:20"),
-> (8,"Daniel","daniel","testdaniel",789,now());


![截圖 2023-08-01 下午10.12.43.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f2d40e27-1c25-46eb-95b0-45daca859dc6/%E6%88%AA%E5%9C%96_2023-08-01_%E4%B8%8B%E5%8D%8810.12.43.png)

mysql>select*from member order by time desc;

![截圖 2023-08-01 下午10.20.38.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6d75465f-b5c6-4a0b-a739-c2cbaab40865/%E6%88%AA%E5%9C%96_2023-08-01_%E4%B8%8B%E5%8D%8810.20.38.png)

mysql>select*from member order by time desc limit 1,3;

![截圖 2023-08-01 下午10.22.19.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/de837aa4-e6b9-4a75-ba6a-b08845a8f3e9/%E6%88%AA%E5%9C%96_2023-08-01_%E4%B8%8B%E5%8D%8810.22.19.png)

mysql>select*from member where username="test";

![截圖 2023-08-01 下午10.24.08.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4e6bca74-99f1-4b10-9467-0b5362191e6a/%E6%88%AA%E5%9C%96_2023-08-01_%E4%B8%8B%E5%8D%8810.24.08.png)

mysql>select*from member where username="test" and password="test";

![截圖 2023-08-01 下午10.24.57.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f821af4c-50af-47a1-9f2b-da7564ba79d0/%E6%88%AA%E5%9C%96_2023-08-01_%E4%B8%8B%E5%8D%8810.24.57.png)

mysql>update member set username="test2" where id=1;

![截圖 2023-08-01 下午10.27.43.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/997548c2-5ffc-4a0c-86e0-c2fd966f6780/%E6%88%AA%E5%9C%96_2023-08-01_%E4%B8%8B%E5%8D%8810.27.43.png)

任務四

mysql>select count(id) from member;

![截圖 2023-08-01 下午11.18.08.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8730c99f-0f8e-465c-babb-9e7eddc3121e/%E6%88%AA%E5%9C%96_2023-08-01_%E4%B8%8B%E5%8D%8811.18.08.png)

mysql>select sum(follower_count) from member;

![截圖 2023-08-01 下午11.19.01.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8672da7b-7e8c-4883-9c3f-da0f09cc6f9e/%E6%88%AA%E5%9C%96_2023-08-01_%E4%B8%8B%E5%8D%8811.19.01.png)

mysql>select avg(follower_count) from member;

![截圖 2023-08-01 下午11.19.36.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/48810a81-7fde-49ba-bddc-e52e49d90923/%E6%88%AA%E5%9C%96_2023-08-01_%E4%B8%8B%E5%8D%8811.19.36.png)

要求五

mysql> create table message(
-> id bigint primary key auto_increment,
-> member_id bigint not null,
-> content varchar(255) not null,
-> like_count int unsigned not null default 0,
-> time datetime not null default current_timestamp);

mysql> alter table message add foreign key(member_id) references member(id);

![截圖 2023-08-01 下午11.31.26.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0fa69e41-4b92-4ce3-88a2-0fe25e2577c9/%E6%88%AA%E5%9C%96_2023-08-01_%E4%B8%8B%E5%8D%8811.31.26.png)

mysql> select [member.name](http://member.name/), message.content from member
-> inner join message on member.id=message.member_id;

![截圖 2023-08-02 下午8.00.26.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/73f48e2f-efb0-446a-a3bc-0691f4ea39e6/%E6%88%AA%E5%9C%96_2023-08-02_%E4%B8%8B%E5%8D%888.00.26.png)

mysql> select [member.name](http://member.name/), message.content from member
-> inner join message on member.id=message.member_id where member.username="test";

![截圖 2023-08-02 下午8.22.10.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a0e7632c-a84e-4d52-8fdd-84ce17f97f01/%E6%88%AA%E5%9C%96_2023-08-02_%E4%B8%8B%E5%8D%888.22.10.png)

mysql> select member.username, avg(message.like_count) from member
-> inner join message on member.id=message.member_id where member.username="test" group by message.member_id;

![截圖 2023-08-02 下午8.45.39.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f29c0797-f59f-484d-9e6f-44ef3c3f29b7/%E6%88%AA%E5%9C%96_2023-08-02_%E4%B8%8B%E5%8D%888.45.39.png)
