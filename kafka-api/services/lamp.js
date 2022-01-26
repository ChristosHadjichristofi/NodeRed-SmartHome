const { Kafka } = require("kafkajs");

const kafka = new Kafka({
    clientId: "lamps-producer",
    brokers: ["localhost:9092"],
});

const topic = "lamps";

const producer = kafka.producer();

const changeLampStatus = async ({ action, roomId }) => {
    try {
        await producer.connect();
        await producer.send({
            topic: topic,
            messages: [{ key: roomId.toString(), value: action }],
        });
        return "OK";
    } catch (err) {
        return "NOT OK";
    }
};

module.exports = { changeLampStatus };
