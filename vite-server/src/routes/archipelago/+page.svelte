<script lang="ts">
	import { Client, clientStatuses } from "archipelago.js"

	const client = new Client();

	client.messages.on("message", (content) => {
		console.log(content);
	});

	function AP_login(IP: string, SLOT: string, PASSWORD: string){
		try {
			client.login(IP, SLOT, "Celeste Classic", {password:PASSWORD})
				.then(() => console.log("connecter to the archipealgo server!"))
				.catch(console.error);
		} catch (error) {
			console.log(error);
		}
	}
	let check_id = $state(0)
	function AP_check(check_id: number) {
		if (!client.authenticated) return
		client.check(check_id)
	}
</script>

<div class="bg-zinc-700 px-2 py-1">
	ARCHIPELGO <br>
	<input
		type="text"
		class="bg-zinc-600 px-2 py-1"
		id="APIP"
		placeholder="IP/Port"
		autocomplete="off"
		value="localhost:38281"
	/>
	<input
		type="text"
		class="bg-zinc-600 px-2 py-1"
		id="APSlot"
		placeholder="SlotName"
		autocomplete="off"
		value="HollowCC"
	/>
	<input
		type="text"
		class="bg-zinc-600 px-2 py-1"
		id="APPassword"
		placeholder="Password"
		autocomplete="off"
	/><br>
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
	</button> <br>
	<button onclick={() => AP_check(check_id)}>Check</button>
	<input type="number" bind:value={check_id}/>
</div>