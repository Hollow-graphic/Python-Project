<script lang="ts">
    let { id, onclick, oncontextmenu } = $props();
    function click(event: MouseEvent) {
        onclick?.(event);
    }
    function rclick(event: MouseEvent) {
        event.preventDefault();
        oncontextmenu?.(event);
    }
</script>

<button
    class="champion"
    style={`background-position: ${-id * 128}px 0px;`}
    title={id}
    onclick={click}
    oncontextmenu={rclick}
></button>

<style>
    .champion {
        width: 128px;
        height: 128px;
        background-image: url("/lol/img/champion.png");
        background-repeat: no-repeat;
    }
</style>