const express = require('express');
const router = express.Router();
const { produceToTopic } = require('../../services/produce-to-topic');

const topic = 'smart-home';

router.post('/', async (req, res) => {
    try {
        const data = req.body;
        const date = Object.keys(data)[0];
        const events = data[date];
        const result = await produceToTopic({ events, date }, topic);
        return res.status(result === 'OK' ? 200 : 500).json({ status: result });
    } catch (err) {
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;
