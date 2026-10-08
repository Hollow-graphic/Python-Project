<script>
    import Case from '../Case.svelte';
    import { onMount } from 'svelte';
    let m = $state();
    let task = $state(["1","2","3","4","5","1","2","3","4","5","1","2","3","4","5","1","2","3","4","5","1","2","3","4","5"]);
    let playerId = $state();

    function resetBingo() {
        m = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]];
    }

    function shuffleBingo() {
        for (let i = task.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [task[i], task[j]] = [task[j], task[i]];
        }
        resetBingo();
    }

    function switchCase(i, j) {
        console.log("CLICK", i, j);
        console.log("Avant :", m[i][j]);
        console.log("player :", idPlayer);

        if (m[i][j] != idPlayer) {
            m[i][j] = idPlayer;
        } else {
            m[i][j] = 0;
        }
        m[i][j] = idPlayer;

        console.log("Après :", m[i][j]);
        console.log($state.snapshot(m));

        if (verify()) {
            shuffleBingo();
        }

        writeBingo();
    }
    
    function verify() {
        // lignes
        for (let i = 0; i < 5; i++) {
            if (
                m[i][0] != 0 && m[i][0] == m[i][1] && m[i][0] == m[i][2] && m[i][0] == m[i][3] && m[i][0] == m[i][4]
            ) {
                return true;
            }
        }

        // colonnes
        for (let i = 0; i < 5; i++) {
            if (
                m[0][i] != 0 && m[0][i] == m[1][i] && m[0][i] == m[2][i] && m[0][i] == m[3][i] && m[0][i] == m[4][i]
            ) {
                return true;
            }
        }

        // diagonale \
        if (
            m[0][0] != 0 &&
            m[0][0] == m[1][1] &&
            m[0][0] == m[2][2] &&
            m[0][0] == m[3][3] &&
            m[0][0] == m[4][4]
        ) {
            return true;
        }

        // diagonale /
        if (
            m[0][4] != 0 &&
            m[0][4] == m[1][3] &&
            m[0][4] == m[2][2] &&
            m[0][4] == m[3][1] &&
            m[0][4] == m[4][0]
        ) {
            return true;
        }

        return false;
    }

    async function getTask() {
        const response = await fetch("/api/getTask");
        const data = await response.json();
        task = data.task;
    }

    async function readTask() {
        const response = await fetch("/api/readTask");
        const data = await response.json();
        task = data.task;
    }

    async function writeBingo() {
        const response = await fetch("/api/writeBingo", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                matrix: $state.snapshot(m)
            })
        });

        const data = await response.json();

        console.log(data);
    }

    async function readBingo() {
        const response = await fetch("/api/readBingo");
        const data = await response.json();

        m = data;
    }

    async function steamStartGame(id) {
        await fetch("/api/steamStartGame", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            id: id
        })
    });
    }
    
    let idPlayer = $state(1);

    resetBingo();
    onMount(() => {
        const params = new URLSearchParams(window.location.search);
        idPlayer = Number(params.get("idPlayer")) || 1;
        readTask();
        readBingo();
    });
    shuffleBingo();
    
</script>

<div id="bingo">
    {#each m as ligne, i}
    <div>
        {#each ligne as valeur, j}
             <Case
                id={valeur}
                onclick={() => switchCase(i, j)}
                text={task[i*5+j]}
            />
        {/each}
    </div>
    {/each}
</div>

<input bind:value={idPlayer} type="number" placeholder="player id" defaultValue="{idPlayer}" id="player">
<br>
<button onclick={shuffleBingo}> Shuffle Bingo</button>

<button onclick={readBingo}>Refresh Bingo</button>

<button onclick={resetBingo}>Reset Bingo</button>
<br>
<button onclick={getTask}>Shuffle Task</button>

<button onclick={readTask}>Refresh Task</button>

<button onclick={() => {steamStartGame("412220")}}>Start DDNet</button>

<style>
    :global(#bingo) {
        display: grid;
        grid-template-columns: repeat(5, 100px);
        grid-template-rows: repeat(5, 100px);
    }
</style>