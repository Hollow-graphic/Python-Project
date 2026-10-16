<script lang="ts">
    import { onMount } from 'svelte';

    let { text }: { text: string } = $props();

    let pos: number = $state(0);
    let cursedText: string = $derived(text)
    let sleepTime = $state(0)

    onMount(() => {
        let timeout: ReturnType<typeof setTimeout>;

        function update() {
            if (pos <= text.length) {
                pos++;
                sleepTime++;
                timeout = setTimeout(update, Math.max(1, 30 - sleepTime * 0.5));
                let chars = cursedText.split("");
                for (let i = 0; i < chars.length; i++) {
                    if (cursedText[i] === '\n' || cursedText[i] === ' ') continue
                    let c = String.fromCharCode(cursedText.charCodeAt(i) + 1)
                    if (c >= 'z') { c = 'a'}
                    cursedText = cursedText.slice(0, i) + c + cursedText.slice(i + 1);
                }
            }
        }

        timeout = setTimeout(update, 40);

        return () => clearTimeout(timeout);
    });
</script>

<div class="whitespace-pre-line inline">
    {text.slice(0, pos)}</div><div class="inline GlichedText">{cursedText.slice(pos)}
</div>

<style>
    .GlichedText {
        font-family: 'Minecraft-enchantment', monospace;
    }
    @font-face {
        font-family: 'Minecraft-enchantment';
        src: url('fonts/minecraft-enchantment.ttf') format('woff2');
        font-weight: 400;
        font-style: normal;
        font-display: swap;
    }
</style>