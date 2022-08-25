<script>
export default {
  data() {
    return {
        ping: ''
    }
  },
  methods: {
    async pinging() {
        try {
            const res = await fetch('http://localhost:8001/ping')
            this.ping = await res.text()
        } catch (err) {
            console.log(err)
            this.ping = 'error!'
        }
    }
  }
}
</script>

<template>
    <div class="pingpong">
    <h1>Click the button</h1>
    <button @click="pinging">Ping... {{ ping }}</button>
    </div>
</template>