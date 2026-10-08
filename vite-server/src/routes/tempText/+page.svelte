<script>
    let text = $state("")
    async function send() {
        const response = await fetch(
            "/api/tempText",
            {
                method: "POST",
                body: text
            }
        );
    }
</script>

<button>Send</button>

<textarea bind:value={text}></textarea>