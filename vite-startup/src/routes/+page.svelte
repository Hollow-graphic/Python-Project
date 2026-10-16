<script lang="ts">
	import Header from '$lib/components/Header.svelte';
    import Project from '$lib/components/Project.svelte';
    import Block from '$lib/components/Block.svelte';
    import GlichedText from '$lib/components/GlichedText.svelte';
	import { clickToCopy } from "./clickToCopy.js";


	let isTabOpen = $state(false)
	let isMoreOption = $state(true)
	let whichTab = $state("about me")
	let isMuted = $state(true)
	let video: HTMLVideoElement;

</script>

<svelte:window
	//onkeydown={(ev) => {if (ev.key === 'z' && (ev.ctrlKey || ev.metaKey)) undo();}}
/>


<!-- Tab div -->
<div  class="fixed m-2 bg-zinc-800/80 rounded-lg shadow-lg z-20">
	<button onclick={() => {isTabOpen = !isTabOpen}} style={"font-size: xx-large;"}> ≡ </button>
	{#if isTabOpen}
	<div
		class="fixed text-zinc-50 bg-zinc-800/80 rounded-lg shadow-lg m-1" 
		style={`height:88%; width:20%`}
	>
	</div>
	{/if}
</div>

<div class="fixed bg-zinc-800/80 bottom-0 left-0 m-2 rounded-lg shadow-lg z-20">
	<button onclick={() => {isMuted = !isMuted; video.muted = isMuted}} style={"font-size: large;"}> Music: {isMuted? "OFF" : "ON"} </button>
</div>


<main class="flex items-center flex-col h-full w-full absolute">
	<video
		bind:this={video}
        autoplay
        loop
        muted={isMuted}
        playsinline
        class="absolute inset-0 w-full h-full object-cover object-center z-0"
    >
        <source src="/img/Paint2.mp4" type="video/mp4" />
    </video>
	<div class="z-10 p-8">
	</div>
	<div class="flex gap-8 z-10">
		<div class="flex bg-zinc-900/80 w-96 h-[80vh] rounded-lg shadow-lg shadow-rose-500/50 grid grid-rows-4" style={""}>
			<div class="rounded-lg">
				<div class="grid grid-cols-2">
					<img alt="pfp" class="h-48 w-48 bg-zinc-700 shadow-lg shadow-rose-500/20" src="ttps://cdn.discordapp.com/avatars/842920374954098738/3177621de1d6428060ffd28881700735.webp"/>
					<div class="h-full w-full p-2"></div>
				</div>
			</div>
			<Block>
				<GlichedText text="this is a text message iuzgduyqhgziufqugfdiqzgdiqzibqzidhkb"></GlichedText>
			</Block>
		</div >
		<div class="flex-col h-[80vh] bg-zinc-900/80 gap-4 rounded-lg shadow-lg shadow-rose-500/50" style={"width: 512px"}>
			<div class="p-2">
				<button class="bg-zinc-700/50 rounded-lg p-1 inset-shadow-sm inset-shadow-rose-500" onclick={() => {whichTab = "About Me"}}> About Me </button>
				<button class="bg-zinc-700/50 rounded-lg p-1 inset-shadow-sm inset-shadow-rose-500" onclick={() => {whichTab = "My Project"}}> Project </button>
				<button class="bg-zinc-700/50 rounded-lg p-1 inset-shadow-sm inset-shadow-rose-500" onclick={() => {whichTab = "Link"}}> Link </button>
			</div>
			{#if whichTab === "My Project"}
				<div class="Project-tab rounded-lg inligne h-400">

					<Project title="Lol build" text="help you build your item" link="lol"></Project>
					<Project title="Bingo" text="custom game challenge" link="bingo"></Project>
					<Project title="Archipelago" text="test archipelago game" link="archipelago"></Project>
					<!--<button class="felx bg-blue-700 rounded-lg h-8 w-16"> Join </button>-->
					
				</div>
			{:else if whichTab === "Link"}
				<div class="Project-tab flex rounded-lg inligne overflow-visible overflow-y-auto h-400 gap-8">
					<a href="https://github.com/Hollow-graphic">
						<button class="h-24 w-24 rounded-lg bg-zinc-700/50 shadow-lg shadow-rose-500/20">
							<img class="flex" alt="github" src="/logo/github.png" height="100%" width="100%"/>
						</button>
					</a>
					<button use:clickToCopy={'adam.autin@epitech.eu'} class="h-24 w-24 rounded-lg bg-zinc-700/50 shadow-lg shadow-rose-500/20">
						<img class="flex" alt="github" src="/logo/gmail.png" height="100%" width="100%"/>
					</button>
					<button use:clickToCopy={'hollow_craft'} class="h-24 w-24 rounded-lg bg-zinc-700/50 shadow-lg shadow-rose-500/20">
						<img class="flex" alt="github" src="/logo/discord.png" height="100%" width="100%"/>
					</button>
				</div>
			{:else}
				<div class="Project-tab rounded-lg inligne overflow-visible overflow-y-auto h-400">
					<Block>
						<div class="font-bold p-1">Current Activity:</div>
        				<div class="item-center border-l border-zinc-400 border"></div>
						<div class="p-2">
							<GlichedText text={'Studying at Epithech. First year of three.\nLearning TS and working on this page'}></GlichedText>
						</div>
					</Block>
				</div>
			{/if}
		</div>
	</div>
</main>

<style>
	.Project-tab {
		height: 600px; 
		width: 100%; 
		scroll-behavior: smooth;
		padding: 5px;
	}
</style>