playlist = dict(
    title="my playlist",
    author="john doe",
    songs=[
        dict(song_title="Turn It Off", artist="Culture Abuse",
             album="Peach", duration=2.5, date="2017-10-31", rating=3.37),
        dict(song_title="Nights Off", artist="Siriamo",
             album="Mosaik", duration=5.2, date="2017-11-06", rating=4.08),
    ])

print(playlist)

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
print(f"total duration of playlist: {total_length}")
