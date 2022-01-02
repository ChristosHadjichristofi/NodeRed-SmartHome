const { Kafka } = require('kafkajs');
const { partitionsPerDevice } = require('../../data/devices-partitions');

const kafka = new Kafka({
    clientId: 'nodered-events-producer',
    brokers: ['localhost:9092'],
});

const producer = kafka.producer();

const produceToTopic = async (events, topic = 'smart-home-events') => {
    await producer.connect();
    for (let event in events) {
        await producer.send({
            topic: topic,
            messages: [{ key: event, value: JSON.stringify(events[event]), partition: partitionsPerDevice[event] }],
        });
    }
};

module.exports = { produceToTopic };
