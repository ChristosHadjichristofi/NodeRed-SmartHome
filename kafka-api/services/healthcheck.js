const mysql = require("mysql");

const checkDbHealth = () => {
    const con = mysql.createConnection({
        host: "localhost",
        port: 3311,
        user: "root",
        password: "root",
    });
    con.connect(function (err) {
        if (err) throw err;
    });
    return "UP";
};

module.exports = { checkDbHealth };
