const data = require('./data.json')

module.exports = function () {
    const max = data.quotes.length
    const random = Math.floor(Math.random() * max)

    return data.quotes[random]
}