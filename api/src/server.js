const express = require('express')
const app = express()
const qoutes = require('./quotes')

const host = '0.0.0.0'
const port = 8002

app.get('/', (req, res) => {
  res.send('Qoute Service!')
})

app.get('/quote', (req, res) => {
  res.json(qoutes()).end()
})

app.listen(port, host, () => {
  console.log(`Example app listening on port ${port}`)
})