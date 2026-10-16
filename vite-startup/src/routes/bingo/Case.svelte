<script lang="ts">
    let { id, onclick, text } = $props();

    const color = [0, 240, 120, 60, 180, 300];

    let caseColor = $state("hsl(224, 28%, 29%)");

    $effect(() => {
        if (id === 0) {
            caseColor = "hsl(224, 28%, 29%)";
        } else if (id <= 6) {
            caseColor = `hsl(${color[id - 1]}, 85%, 77%)`;
        }
    });

    function switchColor(event: MouseEvent) {
        onclick?.(event);
    }
</script>

<button
    class="bingo-case text-xs"
    onclick={switchColor}
    style:background-color={caseColor}
>
    {text}
</button>

<style>
    :global(.bingo-case) {
        color: white;
        height: 100px;
        width: 100px;
        margin: 0;
        padding: 0;
        border: 1px solid white;
        box-sizing: border-box;

        transition:
            background-color 0.1s ease-in-out,
            transform 0.5s ease-in-out;
    }

    :global(.bingo-case:hover) {
        transform: scale(1.1);
    }
</style>