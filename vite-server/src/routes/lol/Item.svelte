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
    class="item"
    style={`background-position: ${-id * 64}px 0px;`}
    title={id}
    onclick={click}
    oncontextmenu={rclick}
></button>

<style>
    .item {
        width: 64px;
        height: 64px;
        background-image: url("/lol/img/items.png");
        background-repeat: no-repeat;
    }
</style>