const { Kafka } = require('kafkajs');
const { partitionsPerDevice } = require('../../data/devices-partitions');

const kafka = new Kafka({
    clientId: 'nodered-events-producer',
    brokers: ['localhost:9092'],
});

const producer = kafka.producer();

const produceToTopic = async (events, topic) => {
    try {
        let splicedEvent;
        await producer.connect();
        for (let event in events) {
            if (event === 'alarm' || event === 'sensorSmoke') splicedEvent = event;
            else splicedEvent = event.slice(0, event.length - 1);

            await producer.send({
                topic: topic,
                messages: [{ key: event, value: JSON.stringify(events[event]), partition: partitionsPerDevice[splicedEvent] }],
            });
        }
        return 'OK';
    } catch (err) {
        return 'NOT OK';
    }
};

module.exports = { produceToTopic };
