const { Kafka } = require('kafkajs');
const kafka = new Kafka({
    clientId: 'my-consumer',
    brokers: ['localhost:9092'],
});

const consumer = kafka.consumer({ groupId: 'test-consumer' });

const run = async () => {
    await consumer.connect();
    await consumer.subscribe({ topic: 'node-red-events-v1', fromBeginning: true });
    await consumer.run({
        eachMessage: async (topic, partition, message) => {
            console.log({
                partition,
                offset: message.offset,
                value: message.value.toString(),
            });
        },
    });
};

(async () => {
    try {
        return await run();
    } catch (err) {
        console.error(err);
    }
})();
