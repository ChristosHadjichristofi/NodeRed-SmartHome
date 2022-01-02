const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

/*  
    Producer Route- This endpoint will accept requests
    from our simulation script and produce records
    to the correct kafka topic
*/

app.use('/events', require('./routes/events/producer.js'));

app.listen(PORT, () => console.log(`Server running on port: ${PORT}`));
