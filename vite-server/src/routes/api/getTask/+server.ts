import { writeFile } from "fs/promises";

export async function GET() {
    const response = await fetch("http://127.0.0.1:5000/bingo/getTask");
    const data = await response.json();

    await writeFile(
        "task.json",
        JSON.stringify(data, null, 4),
        "utf-8"
    );

    return new Response(JSON.stringify(data), {
        headers: {
            "Content-Type": "application/json"
        }
    });
}