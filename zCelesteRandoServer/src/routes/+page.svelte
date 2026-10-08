<script lang="ts">
	import Error from '$lib/components/Error.svelte';
	import LevelBox from '$lib/components/LevelBox.svelte';
	import LevelButton from '$lib/components/LevelButton.svelte';
	import {
		persist_state,
		persist_levels,
		type Level,
	} from '$lib/persist.svelte';
	import ShareButton from '$lib/components/ShareButton.svelte';
	import { plural } from '$lib/util';
	import Loading from '$lib/components/Loading.svelte';
	import Header from '$lib/components/Header.svelte';

	let initial_skips = persist_state('initial_skips', 1);

	const levels = persist_levels();

	const deltaSkips = {
		full_cleared: 1,
		golden: 3,
		skipped: -1,
	};

	let cancelAdd: AbortController | null = null;

	import readline from "node:readline"
	import { Client } from "archipelago.js"

	const client = new Client();
	let is_connect = $state(false)
	let ap_id_start = $state(-1)
	let ap_strawberry_id = $state(10)
	let ap_strawberry_max = $state(15)


	client.messages.on("message", (content) => {
		console.log(content);
	});

	

	async function addLevel(skips: number) {
		levels.push({
			url: "crypto.randomUUID()",
			status: 'loading',
			skips_at_start: skips,
		});
		cancelAdd?.abort();
		cancelAdd = new AbortController();
		const res = await fetch('/api/random');
		if (cancelAdd.signal.aborted) {
			return;
		}
		if (!res.ok) {
			const { message, details } = await res.json().catch(() => ({
				message: 'Unexpected error',
				details: 'API returned invalid JSON',
			}));
			levels.set_last({
				url: "crypto.randomUUID()",
				status: 'error',
				message,
				details,
				skips_at_start: skips,
			});
			return;
		}
		const data = await res.json<Level>();
		if (cancelAdd.signal.aborted) {
			return;
		}
		levels.set_last({
			...data,

			skips_at_start: skips,
			status: 'in_progress',
		});
	}
	async function reroll() {
		const error = levels.pop();
		return addLevel(error?.skips_at_start ?? initial_skips.value);
	}
	async function nextLevel(status: Level['status']) {
		const lastLevel = levels.last;
		if (lastLevel?.status !== 'in_progress') return;
		if (status !== 'skipped' && status !== 'failed' && status !== 'unfinished') AP_check(levels.length - ap_id_start)
		lastLevel.status = status;
		const skipDelta = deltaSkips[status as keyof typeof deltaSkips] ?? 0;
		await addLevel(lastLevel.skips_at_start + skipDelta);
	}
	async function register(status: Level['status']) {
		const lastLevel = levels?.last;
		if (lastLevel == undefined) return;
		const id = lastLevel.url?.split('/').pop();
		let progression = '';
		if (status == 'unfinished') {
			progression += '-' + prompt('how many room did you complete and how many in total')
		}
		if (status == 'golden') {
			progression += '-' + prompt('what is the total death and time');
		}
		const text = id + progression;
		await fetch(`/api/${status}`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				text: text,
			}),
		});
		if (status == 'complete') status = 'cleared';
		if (status == 'unfinished') status = 'cleared';
		nextLevel(status);
	}
	async function gameOver() {
		const level = levels.last;
		if (!level) return;
		level.status = 'failed';
	}
	const cumulativeClears = $derived.by(() => {
		const cum: number[] = [];
		let sum = 0;
		for (const level of levels.array) {
			if (level.status === 'cleared' || level.status === 'full_cleared' || level.status === 'golden') sum++;
			cum.push(sum);
		}
		return cum;
	});

	function undo() {
		cancelAdd?.abort();
		if (levels.last?.status === 'failed') {
			levels.last.status = 'in_progress';
			return;
		}
		levels.pop();
		const lastLevel = levels.last;
		if (!lastLevel) return;
		lastLevel.status = 'in_progress';
	}

	let container: HTMLElement;
	$effect(() => {
		levels.last;
		const last = container?.lastElementChild as HTMLElement;
		if (last) last.scrollIntoView({ behavior: 'smooth' });
	});

	let isTabOpen = $state(false)
	let isMoreOption = $state(true)

	async function mod_download(mod_url: string) {
        const mod_id = mod_url.split("/mods/")[1]
        const data = await fetch(`https://gamebanana.com/apiv8/Mod/${mod_id}?_csvProperties=_idRow,_sName,_aFiles`).then(r => r.json());
        window.open(`everest:https://gamebanana.com/dl/${data._aFiles[0]._sDownloadUrl.split("/").at(-1)}?`, "_blank")
    }

	function AP_login(IP: string, SLOT: string, PASSWORD: string){
		try {
			client.login(IP, SLOT, "Celeste Classic", {password:PASSWORD})
				.then(() => console.log("connecter to the archipealgo server!"))
				.catch(console.error);
			ap_id_start = levels.length
			if (client.authenticated) is_connect = true; else is_connect = false
		} catch (error) {
			console.log(error);
			ap_id_start = -1
		}
	}
	function AP_check(check_id: number) {
		console.log(client.authenticated)
		if (!client.authenticated) return
		console.log(check_id)
		client.check(check_id)
	}
</script>

<svelte:window
	onkeydown={(ev) => {
		if (ev.key === 'z' && (ev.ctrlKey || ev.metaKey)) undo();
	}}
/>

{#if levels.length > 0}
	<div class="fixed text-zinc-50 bottom-0 left-0 m-2">
		{#if levels.last?.status === 'in_progress'}
			<LevelButton icon="skull" onclick={gameOver} class="text-red-300">
				Give Up Early
			</LevelButton>
			<LevelButton
				icon="skip"
				onclick={() => {
					const lastLevel = levels.last;
					if (lastLevel) lastLevel.skips_at_start += 5;
				}}
				class="text-yellow-300"
			>
				Add 5 Skips
			</LevelButton>
		{/if}
		<p>
			<kbd>CTRL</kbd> + <kbd>Z</kbd> to undo
		</p>
	</div>
{/if}

<div  class="fixed m-2 bg-zinc-800 rounded-lg shadow-lg">
	<button onclick={() => {isTabOpen = !isTabOpen}} style={"font-size: xx-large;"}> ≡ </button>
	{#if isTabOpen}
	<div
		class="fixed text-zinc-50 bg-zinc-800 rounded-lg shadow-lg" 
		style={`height:90%; width:20%`}
	> 
		<div class="bg-zinc-700 px-2 py-1">
			ARCHIPELGO <br>
			<input type="text" class="bg-zinc-600 px-2 py-1" id="APIP" placeholder="IP/Port" autocomplete="off" value="localhost:38281"/>
			<input type="text" class="bg-zinc-600 px-2 py-1" id="APSlot" placeholder="SlotName" autocomplete="off" value="HollowCC"/>
			<input type="text" class="bg-zinc-600 px-2 py-1" id="APPassword" placeholder="Password" autocomplete="off" />
			<br>
			<button
				class="btn mt-2"
				id="loginButton"
				onclick={() =>
					AP_login(
						(document.getElementById('APIP') as HTMLInputElement).value,
						(document.getElementById('APSlot') as HTMLInputElement).value,
						(document.getElementById('APPassword') as HTMLInputElement).value,
					)}
			>Login
			</button>
			{#if is_connect}
				<div style={"color:green"}> CONNECTED</div>
			{:else}
				<div style={"color:red"}> NOT CONNECTED</div>
			{/if}
			{ap_id_start}
			{levels.length - ap_id_start}
			{ap_strawberry_id}
			<div class="bg-zinc-700 px-2 py-1">
				More Option: <input bind:checked={isMoreOption} type="checkbox"/>
			</div>
			<div style={"height: 400px; overflow-y: scroll; scroll-behavior: smooth"}>
				 -- Funny Check --
			<br> Unintentional Dashless Room <input onclick={() => AP_check()} type="checkbox"/>
			<br> One of the Hardest Map
			<br> Awake Song
			<br> Find Easter Egg
			<br> B-side Clear
			<br> Variant Map
			<br> Birthday Map
			<br> Everest Installer Error
			<br> Already Beaten
			<br> Already Golden
			<br> Low Effort Map
			<br> Art Thumbnail
			<br> Random Thumnail
			<br> Nonsence Map Name
			<br> WIP Map
			<br> All Capital Map Name
			<br> Other Language Map
			<br> 20+ Room Map
			<br> Collab submission
			<br> Vanilla only
			<br> -- Challenge --
			<br> 100% Golden
			<br> 3 Winged Berry in total
			</div>
		<button onclick={() => AP_check(levels.length - ap_id_start)}>[Send Check]</button>
		</div>
	</div>
	{/if}
</div>

{#snippet skipLine(text: string, plus1 = false)}
	<div class="border-l border-zinc-400 border-dashed h-8 my-1" />
	{#if plus1}
		<p class="text-purple-400 mt-1">+1 SKIP</p>
	{/if}
	<p class="text-sm text-zinc-400 uppercase">{text}</p>
	<div class="border-l border-zinc-400 border-dashed h-8 my-1" />
{/snippet}

<main
	bind:this={container}
	class="flex items-center flex-col max-w-screen-lg mx-auto p-8"
>
	<Header />
	<label>
		Start with skips:
		<select
			disabled={levels.length > 0}
			class="bg-zinc-700 px-2 py-1"
			bind:value={initial_skips.value}
		>
			{#each Array.from({ length: 11 }, (_, i) => i) as i}
				<option value={i}>{i}</option>
			{/each}
		</select>
	</label>
	<button
		class="btn mt-2"
		disabled={levels.length > 0}
		onclick={() => addLevel(initial_skips.value)}
	>
		Begin
	</button>
	{#if levels.length > 0}
		{@render skipLine(
			`Start, ${initial_skips.value} ${plural('skip', initial_skips.value)}`,
		)}
	{/if}
	{#each levels.array as level, i (level.url)}
		{#if level.status === 'error'}
			<Error {level} onretry={reroll} />
		{:else if level.status === 'loading'}
			<Loading />
		{:else}
			<LevelBox
				{level}
				onreroll={reroll}
				onclear={() => nextLevel('cleared')}
				onfc={() => register('full_cleared')}
				ongolden={() => register('golden')}
				onskip={() => nextLevel('skipped')}
				oncomplete={() => register('complete')}
				onfail={gameOver}
				ontrash={() => register('trash')}
				onunfinished={() => register('unfinished')}
				ondownload={() => mod_download(level.url)}
				onstrawberry={() => {AP_check(ap_strawberry_id); if (ap_strawberry_id < ap_strawberry_max) {ap_strawberry_id += 1}}}
				ismoreoption={isMoreOption}
				isarchipelago={true}
			/>
		{/if}
		{#if i < levels.length - 1}
			{@const               skips = levels.i(i + 1)!.skips_at_start}
			{@const               clears = cumulativeClears[i]!}
			{@render skipLine(
				`${clears} ${plural('clear', clears)}, ${skips} ${plural('skip', skips)}`,
				level.status === 'full_cleared',
			)}
		{/if}
	{/each}
	{#if levels.last?.status === 'failed'}
		{@const clears = cumulativeClears[cumulativeClears.length - 1] ?? 0}
		<div class="border-l border-zinc-400 border-dashed h-8 mt-1" />
		<div class="text-center text-zinc-200 uppercase my-1">
			<p class="text-red-400">Game Over!</p>
			<p class="tabular-nums">Score: {clears} {plural('clear', clears)}.</p>
		</div>
		<button
			class="btn my-2"
			onclick={() => {
				levels.clear();
			}}
		>
			Play Again
		</button>
		<ShareButton levels={levels.array} initial_skips={initial_skips.value} />
	{/if}
	<div class="h-[300px]" />
</main>
