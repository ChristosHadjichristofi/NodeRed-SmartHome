const express = require('express');
const router = express.Router();
const { produceToTopic } = require('../../services/produce-to-topic');

router.get('/', async (req, res) => {
    try {
        const events = req.body;
        await produceToTopic(events);
        
        return res.status(201).json({ msg: 'Records added successfully!' });
    } catch (err) {
        console.error(err);
        res.status(500).send('Internal Server Error');
    }
});

module.exports = router;
