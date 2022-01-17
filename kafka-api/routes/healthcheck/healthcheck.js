const express = require("express");
const { checkDbHealth } = require("../../services/healthcheck");
const router = express.Router();

router.get("/serverStatus", async (req, res) => {
    return res.status(200).json({ status: "UP" });
});

router.get("/dbHealth", async (req, res) => {
    const result = await checkDbHealth();
    return res.status(200).json({ status: result });
});

module.exports = router;
