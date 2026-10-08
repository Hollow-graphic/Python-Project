import { writeFile } from "fs/promises";

export async function POST({ request }) {
    const { matrix } = await request.json();

    await writeFile(
        "bingo.json",
        JSON.stringify(matrix, null, 4),
        "utf-8"
    );

    return new Response(
        JSON.stringify({ status: "success" }),
        {
            headers: {
                "Content-Type": "application/json"
            }
        }
    );
}