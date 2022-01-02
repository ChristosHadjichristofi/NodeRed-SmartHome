const express = require('express');
const app = express();
const PORT = 3000;

/*  
    Producer Route- This endpoint will accept requests
    from our simulation script and produce records
    to the correct kafka topic
*/

app.use('/events', require('./routes/events/producer.js'));

app.listen(PORT, () => console.log(`Server running on port: ${PORT}`));
