import { appendFile } from 'fs/promises';

export async function POST({ request }) {
    const { text } = await request.json();

    await appendFile("full_cleared.txt", text + "\n");

    return new Response("OK");
}
