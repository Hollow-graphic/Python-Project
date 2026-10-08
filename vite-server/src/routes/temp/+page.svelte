<script>
    import xml from './modsettings-Hyperline.celeste?raw'

    let nb = $state(5);

    // HSL encodé : HHHSSSLLL
    let color = $state([
        0,
        0,
        0,
        0,
        0
    ]);

    function hslToCss(value) {
        value = String(value).padStart(9, "0");

        const h = Number(value.slice(0, 3));
        const s = Number(value.slice(3, 6));
        const l = Number(value.slice(6, 9));

        return `hsl(${h}, ${s}%, ${l/2}%)`;
    }

    function hslToRgb(value) {
        value = String(value).padStart(9, "0");

        const h = Number(value.slice(0, 3));
        const s = Number(value.slice(3, 6)) / 100;
        const l = Number(value.slice(6, 9)) / 100;

        const c = (1 - Math.abs(2 * l - 1)) * s;
        const x = c * (1 - Math.abs((h / 60) % 2 - 1));
        const m = l - c / 2;

        let r = 0, g = 0, b = 0;

        if (h < 60) {
            r = c; g = x;
        } else if (h < 120) {
            r = x; g = c;
        } else if (h < 180) {
            g = c; b = x;
        } else if (h < 240) {
            g = x; b = c;
        } else if (h < 300) {
            r = x; b = c;
        } else {
            r = c; b = x;
        }

        return [
            Math.round((r + m) * 255),
            Math.round((g + m) * 255),
            Math.round((b + m) * 255)
        ];
    }

    function rgbToHsl(r, g, b) {
        r /= 255;
        g /= 255;
        b /= 255;

        const max = Math.max(r, g, b);
        const min = Math.min(r, g, b);

        let h = 0;
        let s = 0;
        const l = (max + min) / 2;

        if (max !== min) {
            const d = max - min;

            s = l > 0.5
                ? d / (2 - max - min)
                : d / (max + min);

            switch (max) {
                case r:
                    h = (g - b) / d + (g < b ? 6 : 0);
                    break;
                case g:
                    h = (b - r) / d + 2;
                    break;
                case b:
                    h = (r - g) / d + 4;
                    break;
            }

            h *= 60;
        }

        return [
            Math.round(h),
            Math.round(s * 100),
            Math.round(l * 200)
        ];
    }

    function rgbToNumber(r, g, b) {
        const [h, s, l] = rgbToHsl(r, g, b);

        return h * 1000000 + s * 1000 + l;
    }

    function colorChanged(event, i) {
        const rgb = event.currentTarget.value;

        const r = parseInt(rgb.slice(1, 3), 16);
        const g = parseInt(rgb.slice(3, 5), 16);
        const b = parseInt(rgb.slice(5, 7), 16);

        color[i] = rgbToNumber(r, g, b);
    }
</script>

<input bind:value={nb} type="number"/>

<div>
    {#each Array(parseInt(nb, 10)) as _, i}

        <!-- Color picker -->
        <input
            type="color"
            value="#000000"
            oninput={(event) => colorChanged(event, i)}
        />

        <!-- Aperçu -->
        <div
            style:height="100px"
            style:width="100px"
            style:background-color={hslToCss(color[i])}
        ></div>

        <!-- Valeur HSL encodée -->
        <input
            type="text"
            bind:value={color[i]}
        />
        <br>
    {/each}
</div>

<p>{xml}</p>