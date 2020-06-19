import wget

url = "http://xyz.ij/Series/HomeWatch/S{season}/480p/HomeWatch.S{season}E{episode}.480p.mkv"
first_season, last_season = 5, 8
episode_count = 12

for season in range( first_season, last_season + 1):
    episode = 1
    while episode <= episode_count:
        print(f"\nSeason: {season}\nepisode: {episode}\n")
        wget.download(
                url.format(
                    season=str(season).rjust(2, "0"),
                    episode=str(episode).rjust(2, "0")
            )
        )
        episode += 1

