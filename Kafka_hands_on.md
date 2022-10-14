### Download and extract Kafka
- wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz
- tar -xzf kafka_2.12-2.8.0.tgz
- cd kafka_2.12-2.8.0

### start ZooKeeper
- bin/zookeeper-server-start.sh config/zookeeper.properties

### Start the Kafka broker service
- cd kafka_2.12-2.8.0
- bin/kafka-server-start.sh config/server.properties

### Create a topic
- cd kafka_2.12-2.8.0
- bin/kafka-topics.sh --create --topic news --bootstrap-server localhost:9092

### Start Producer
- bin/kafka-console-producer.sh --topic news --bootstrap-server localhost:9092
- write
```
Good morning
Good day
Enjoy the Kafka lab
```

### Start Consumer
- cd kafka_2.12-2.8.0
- bin/kafka-console-consumer.sh --topic news --from-beginning --bootstrap-server localhost:9092

### Create a new topic named weather
- cd kafka_2.12-2.8.0
- bin/kafka-topics.sh --create --topic weather --bootstrap-server localhost:9092

### Post messages to the topic weather
- bin/kafka-console-producer.sh --topic weather --bootstrap-server localhost:9092

### Read the messages from the topic weather
- cd kafka_2.12-2.8.0; bin/kafka-console-consumer.sh --topic weather --from-beginning --bootstrap-server localhost:9092

### create a new topic called bankbranch
- cd kafka_2.12-2.8.0
- bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic bankbranch  --partitions 2

### list topics
- bin/kafka-topics.sh --bootstrap-server localhost:9092 --list

### describe topic
- bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic bankbranch

### Create a producer for topic bankbranch
- bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic bankbranch
- {"atmid": 1, "transid": 100}
- {"atmid": 1, "transid": 101}
- {"atmid": 2, "transid": 200}
- {"atmid": 1, "transid": 102}
- {"atmid": 2, "transid": 201}

### consumer to subscribe topic bankbranch
- cd kafka_2.12-2.8.0
- bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --from-beginning

### In this step, you will be using message keys to ensure messages with the same key will be consumed with the same order as they published.
- bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic bankbranch --property parse.key=true --property key.separator=:
- 1:{"atmid": 1, "transid": 102}
- 1:{"atmid": 1, "transid": 103}
- 2:{"atmid": 2, "transid": 202}
- 2:{"atmid": 2, "transid": 203}
- 1:{"atmid": 1, "transid": 104}
- bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --from-beginning --property print.key=true --property key.separator=:

### create a consumer group
- bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --group atm-app
- bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group atm-app
- 1:{"atmid": 1, "transid": 105}
- 2:{"atmid": 2, "transid": 204}
- bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group atm-app
- bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --group atm-app

### Reset offset
- bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092  --topic bankbranch --group atm-app --reset-offsets --to-earliest --execute
- bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --group atm-app
- bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092  --topic bankbranch --group atm-app --reset-offsets --shift-by -2 --execute
- bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --group atm-app

