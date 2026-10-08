export async function POST({ request }) {
    const body = await request.json();

    const response = await fetch("http://127.0.0.1:5000/steam/startGame", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body)
    });

    const data = await response.json();

    return new Response(JSON.stringify(data), {
        headers: {
            "Content-Type": "application/json"
        }
    });
}