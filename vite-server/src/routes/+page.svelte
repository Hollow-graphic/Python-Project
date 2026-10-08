<script>

    async function steamStartGame(id) {
        await fetch("/api/steamStartGame", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                id: id
            })
        });
    }
</script>

<button onclick={() => {steamStartGame("412220")}}>Start DDNet</button>

<button onclick={() => window.location.href = "/bingo"}>Bingo</button>
<button onclick={() => window.location.href = "/lol"}>Leaque of Legend</button>
<button onclick={() => window.location.href = "/archipelago"}>Archipelago</button>