<script lang="ts">
    let { title, text, link} = $props();
</script>

<div>
    <button
        class="Project rounded-lg bg-zinc-700 shadow-lg hover:shadow-rose-500/50"
        onclick={() => window.location.href = window.location.href + link}
    >
        <div class="flex ">
            <div class="flex h-24 w-24 bg-zinc-700/50 p-1 border-r-2 bg-zinc-800">
                <img class="flex" alt="github" src="/logo/{link}.png"/>
            </div>
            <div class="text-left p-2">
                <div>
                    {title}
                </div>
                <div>
                    {text}
                </div>
            </div>
        </div>
        <!--<div class="item-center border-l border-zinc-400 border"/>-->
    </button>
</div>
<style>
    :global(.Project) {
        height: 100px;
        width: 80%;
        box-sizing: border-box;
        margin-top: 3px;

        transition:
            transform 0.5s ease-in-out,
            box-shadow 0.4s ease-in-out;
    }

    :global(.Project:hover) {
        transform: scale(1.02);
        /*box-shadow: 0 0 20px 5px rgba(248, 56, 130, 0.7);*/
        box-shadow: 0 0 20px 5px rgba(255, 0, 64, 0.2);
    }
</style>