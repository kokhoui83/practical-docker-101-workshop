<script>
export default {
    data() {
        return {
            quote: '',
            author: ''
        }
    },
    methods: {
        async getRandomQuote() {
            try {
                const res = await fetch('http://localhost:8001/randomquote')
                const data = await res.json()
                this.quote = data.quote
                this.author = data.author
            } catch (err) {
                console.log(err)
                this.randomQuote.qoute = 'error!'
                this.randomQuote.author = 'N/A'
            }
        }
    }
}
</script>

<template>
    <div class="quotes">
        <h2>Quote Of The Day</h2>
        <button @click="getRandomQuote">Get Quote</button>
        <p>{{ quote }}</p>
        <p>~ {{ author }}</p>
    </div>
</template>