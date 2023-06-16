
const functions = require('@google-cloud/functions-framework');
const { lookup } = require('geoip-lite');

functions.http('/', (req, res) => {
    controlLogic(req, res);
});

const controlLogic = (req, res) => {
    const ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    const lookupRes = lookup(ip);
    const country = lookupRes?.country;

    if (country == 'US') {
        res.redirect('https://k8s-ingress-url.com/us');
    } else if (country == 'UAE') {
        res.redirect('https://k8s-ingress-url.com/uae');
    } else {
        res.send(`${country} is not supported country!`)
    }
}