import { connections } from "$lib/server/apollo";

export const POST = async ({ request }) => {
	const { slot, locationId } = await request.json();

	const ws = connections.get(slot);

	if (!ws) {
		return new Response(JSON.stringify({
			ok: false,
			error: "Not connected"
		}), { status: 400 });
	}

	ws.send(JSON.stringify([{
		cmd: "LocationChecks",
		locations: [locationId]
	}]));

	return new Response(JSON.stringify({ ok: true }), { status: 200 });
};