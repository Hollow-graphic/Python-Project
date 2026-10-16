import { writeFile } from "fs/promises";

export async function POST({ request }) {
    const { build } = await request.json();

    await writeFile(
        "src/routes/lol/build.json",
        JSON.stringify(build, null, 4),
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