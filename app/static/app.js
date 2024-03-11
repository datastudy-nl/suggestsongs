let songs_to_rate = [];
let current_track = null;
async function rateTrack(rating) {
    await fetch('/api/rate-track', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ track_id: current_track.track_id, rating })
    });
    if (songs_to_rate.length < 5) await getNextSongs();
    showNextTrack();
}


async function getNextSongs() {
    await fetch('/api/next-songs')
        .then(response => response.json())
        .then(data => {
            songs_to_rate = data.data;
        });
}

async function showNextTrack() {
    if (songs_to_rate.length < 5) await getNextSongs();
    if (!songs_to_rate) return;
    current_track = songs_to_rate.shift();
    if (!current_track) {
        document.getElementById('song-info').innerText = 'No more songs to rate';
        document.getElementById('embed-song').src = '';
        return;
    }
    document.getElementById('embed-song').src = `https://open.spotify.com/embed/track/${current_track.track_id}?theme=0`;

}
showNextTrack();
