<script lang="ts">
    let { children } = $props();
</script>

<div>
    <div class="Project rounded-lg bg-zinc-700 shadow-lg shadow-rose-500/20">
        {@render children?.()}
    </div>
</div>
<style>
    :global(.Project) {
        width: 100%;
        min-height: 100px;
        box-sizing: border-box;
        margin: 3px;

        transition:
            background-color 0.1s ease-in-out,
            transform 0.5s ease-in-out,
            box-shadow 0.4s ease-in-out;
    }

    :global(.Project:hover) {
        transform: scale(1.02);
    }
</style>