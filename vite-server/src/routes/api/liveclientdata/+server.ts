import { Agent } from "undici";

const agent = new Agent({
    connect: {
        rejectUnauthorized: false
    }
});

export async function GET() {
    const response = await fetch(
        "https://127.0.0.1:2999/liveclientdata/allgamedata",
        {
            dispatcher: agent
        }
    );

    return new Response(await response.text(), {
        headers: {
            "Content-Type": "application/json"
        }
    });
}