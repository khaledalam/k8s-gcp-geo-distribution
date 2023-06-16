const functions = require('@google-cloud/functions-framework');
const { lookup } = require('geoip-lite');

/**
 * Responds to any HTTP request.
 * 
 * Entry Point: main
 *
 * @param {!express:Request} req HTTP request context.
 * @param {!express:Response} res HTTP response context.
 */
exports.main = (req, res) => {
    controlLogic(req, res);
};

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