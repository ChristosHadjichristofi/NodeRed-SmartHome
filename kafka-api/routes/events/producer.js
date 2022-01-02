const express = require('express');
const router = express.Router();
const { produceToTopic } = require('../../services/produce-to-topic');

router.post('/', async (req, res) => {
    try {
        const data = req.body;
        const parsedData = data[Object.keys(data)[0]];
        await produceToTopic(parsedData);

        return res.status(201).json({ msg: 'Records added successfully!' });
    } catch (err) {
        console.error(err);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;

/*
const obj = {
    'Mon-00:00': {
        sensorSmoke: { status: 0 },
        sensorLight0: { lm: 0 },
        sensorLight1: { lm: 0 },
        sensorLight4: { lm: 0 },
        sensorMotion1: { status: 0 },
        sensorMotion4: { status: 0 },
        sensorTemp0: { temp: 9, tempDif: 9 },
        sensorTemp1: { temp: 9, tempDif: 9 },
        sensorMagnet0: { status: 0 },
        sensorMagnet1: { status: 0 },
        sensorMagnet2: { status: 0 },
        sensorMagnet3: { status: 0 },
        alarm: { status: 0 },
    },
};
*/
