<script lang="ts">
    let { children } = $props();

    let data;

    async function readBingo() {
        const response = await fetch("/api/getStatus");
        data = await response.json();
    }
</script>

<div>
    <div class="rounded-lg bg-zinc-700 shadow-lg shadow-rose-500/20">
        {@html data}
    </div>
</div>

<style>
</style>