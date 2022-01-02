const { Kafka } = require('kafkajs');
const { partitionsPerDevice } = require('../../data/devices-partitions');

const kafka = new Kafka({
    clientId: 'nodered-events-producer',
    brokers: ['localhost:9092'],
});

const producer = kafka.producer();

const produceToTopic = async (input, topic = 'node-red-events-v1') => {
    await producer.connect();
    
    // for (let device in input) {
    //     await producer.send({
    //         topic: topic,
    //         messages: [{ key: device, value: JSON.stringify(input[device]) }],
    //         partition: devices[device],
    //     });
    // }
};

module.exports = { produceToTopic };
