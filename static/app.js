let songs_to_rate = [];
let current_track = null;
let top_rated_songs = [];


async function rateTrack(rating) {
    await fetch('/api/rate-track', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: current_track.id, rating })
    })
        .catch((error) => {
            console.error('Error:', error);
        });
    showNextTrack();
}


async function getNextSongs() {
    await fetch('/api/next-songs')
        .then(response => response.json())
        .then(data => {
            songs_to_rate = data.data;
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

async function showNextTrack() {
    if (songs_to_rate.length < 2) await getNextSongs();
    if (!songs_to_rate) return;
    current_track = songs_to_rate.shift();
    if (!current_track) {
        document.getElementById('song-info').innerText = 'No more songs to rate';
        document.getElementById('embed-song').src = '';
        return;
    }
    document.getElementById('embed-song').src = `https://open.spotify.com/embed/track/${current_track.id}?theme=0`;

}

// async function getTopRatedTracks() {
//     await fetch('/api/top-rated-songs')
//         .then(response => response.json())
//         .then(data => {
//             top_rated_songs = data.data;
//             document.getElementById('top-rated-songs-list').innerHTML = top_rated_songs.map((song, index) => {
//                 return `<div class="top-rated-item">
//                     <div class="top-rated-item-rating">
//                         ${song.rating}
//                     </div>
//                     <div class="top-rated-item-artist">
//                         ${song.artist}
//                     </div>
//                     <div class="top-rated-item-name">
//                     ${song.name}
//                     </div>
//                 </div>`;
//             }).join('');
//         })
//         .catch((error) => {
//             console.error('Error:', error);
//         });
// }


showNextTrack();
getTopRatedTracks()