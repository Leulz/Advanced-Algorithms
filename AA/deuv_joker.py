nd = [int(x) for x in raw_input().split()]

n = nd[0]
d = nd[1]

songs = [int(x) for x in raw_input().split()]

song_minutes = sum(songs)
rest_for_devu = 10*(n-1)
total_time_songs = song_minutes + (rest_for_devu)

if (total_time_songs) > d:
	print -1
else:
	rest_of_time = d - total_time_songs
	time_for_jokes = (rest_for_devu + rest_of_time) / 5
	print time_for_jokes
