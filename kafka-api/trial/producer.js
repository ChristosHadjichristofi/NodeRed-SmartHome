const { Kafka } = require('kafkajs');

const kafka = new Kafka({
    clientId: 'my-app',
    brokers: ['localhost:9092'],
});

const producer = kafka.producer();
(async () => {
    await producer.connect();
    await producer.send({
        topic: 'node-red-events-v1',
        messages: [{ value: 'partition 1 again', partition: 1 }],
    });
    await producer.disconnect();
})();
