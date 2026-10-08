import { appendFile } from 'fs/promises';

export async function POST({ request }) {
    const { text } = await request.json();

    await appendFile("trash.txt", text + "\n");

    return new Response("OK");
}
