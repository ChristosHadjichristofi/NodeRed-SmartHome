const { Kafka, logLevel } = require('kafkajs');

const { WinstonLogCreator } = require('./logger');

const kafka = new Kafka({
    brokers: ['localhost:9092'],
    logLevel: logLevel.INFO,
    logCreator: WinstonLogCreator,
});

const consumer = kafka.consumer({ groupId: 'test-consumerr' });

(async () => {
    await consumer.connect();
    await consumer.logger();
    await consumer.subscribe({ topic: 'trial2', partition: 0, fromBeginning: true });

    await consumer.run({
        eachMessage: async ({ topic, partition, message }) => {
            console.log(partition);
            console.log({ value: message.value.toString() });
        },
    });
})();
