# libraries
from http.client import BAD_GATEWAY
from flask import Flask, redirect, url_for, render_template, session, request
import pandas as pd
import numpy as np

# import file
df = pd.read_excel('C:/Nikol/PPTI 12/PPTI 12 CAWU 3/Artificial Intelligence/Proyek/Muree/Dataset Muree.xlsx')

# IMPORT DATABASE TO VARIABLE
number = np.array(df["No."])
artis = np.array(df["Artis"])
lagu = np.array(df["Judul Lagu"])

number_temp = np.array(df["No."])
artis_temp = np.array(df["Artis"])
lagu_temp = np.array(df["Judul Lagu"])

number_temp2 = np.array(df["No."])
artis_temp2 = np.array(df["Artis"])
lagu_temp2 = np.array(df["Judul Lagu"])

number_default = np.array(df["No."])
artis_default = np.array(df["Artis"])
lagu_default = np.array(df["Judul Lagu"])

pop = np.array(df["Pop"])
hiphop = np.array(df["Hip-hop"])
rock = np.array(df["Rock"])
indie = np.array(df["Indie"])

genre = np.array([pop, hiphop, rock, indie])
genre_temp = np.array([pop, hiphop, rock, indie])
genre_temp2 = np.array([pop, hiphop, rock, indie])
genre_default = np.array([pop, hiphop, rock, indie])

ninety = np.array(df["90s"])
zero = np.array(df["00s"])
ten = np.array(df["10s"])
twenty = np.array(df["20s"])

years = np.array([ninety, zero, ten, twenty])
years_temp = np.array([ninety, zero, ten, twenty])
years_temp2 = np.array([ninety, zero, ten, twenty])
years_default = np.array([ninety, zero, ten, twenty])

# default user profile
user_profile_genre = np.array([[0.25], [0.25], [0.25], [0.25]])
user_profile_years = np.array([[0.25], [0.25], [0.25], [0.25]])

# default new user profile
new_profile_genre = np.array([[0.25], [0.25], [0.25], [0.25]])
new_profile_years = np.array([[0.25], [0.25], [0.25], [0.25]])

#back to playlist
back_playlist = 0

#picked songs
picked = 0

# flag
flag = 0

# counter
counter = 0

# get genre/year length
length = len(lagu)

# set temp sum array for each song
final_table_temp2 = np.array([0.0 for x in range(length)])
final_table_default = np.array([0.0 for x in range(length)])

# for flask
app = Flask(__name__)

# session
app.secret_key = 'secret'

# redirect to main
@app.route("/")
def redirect_to_main():
    return redirect(url_for("clear"))

# clear current playing song
@app.route("/clear")
def clear():
    session.pop("selected_song", None)
    global counter
    global user_profile_genre
    global user_profile_years
    global new_profile_genre
    global new_profile_years
    global final_table_temp2
    global flag
    global picked
    global back_playlist
    counter = 0
    flag = 0
    back_playlist = 0
    picked = 0
    user_profile_genre = np.array([[0.25], [0.25], [0.25], [0.25]])
    user_profile_years = np.array([[0.25], [0.25], [0.25], [0.25]])
    new_profile_genre = np.array([[0.25], [0.25], [0.25], [0.25]])
    new_profile_years = np.array([[0.25], [0.25], [0.25], [0.25]])
    final_table_temp2 = np.array([0.0 for x in range(length)])
    return redirect(url_for("main"))

# main page
@app.route("/main", methods=['GET', 'POST'])
def main():
    # kalau milih lagu
    global flag
    global user_profile_genre
    global user_profile_years
    global new_profile_genre
    global new_profile_years
    global final_table_temp2
    global counter
    global picked
    global back_playlist
    global length

    if counter > 0 and back_playlist == 0:
        iter = 1
        temp_arr_genre = np.array([[0] * 100 for i in range(4)])
        temp_arr_years = np.array([[0] * 100 for i in range(4)])

        total_genre = np.array([[0] * 1 for i in range(4)])
        total_years = np.array([[0] * 1 for i in range(4)])
        cumulative_genre = 0
        cumulative_years = 0

        while iter <= counter:
            for i in range (4):
                temp_arr_genre[i][iter-1] = genre[i][iter-1]
                total_genre[i][0] += temp_arr_genre[i][iter-1]
                cumulative_genre += temp_arr_genre[i][iter-1]

                temp_arr_years[i][iter-1] = years[i][iter-1]
                total_years[i][0] += temp_arr_years[i][iter-1]
                cumulative_years += temp_arr_years[i][iter-1]
            iter+=1

        # calculate new profile
        profile_temp_genre = np.array(total_genre/cumulative_genre)
        profile_temp_years = np.array(total_years/cumulative_years)

        new_profile_genre = (user_profile_genre*95/100)+(profile_temp_genre*5/100)
        new_profile_years = (user_profile_years*95/100)+(profile_temp_years*5/100)

        # calculate arr * new profile
        genre_profile_table = np.array(genre*new_profile_genre)
        years_profile_table = np.array(years*new_profile_years)

        # set temp sum array for each song
        sum_profile_genre = np.array([0.0 for x in range(length)])
        sum_profile_years = np.array([0.0 for x in range(length)])

        # sum each song genre/years
        for i in range(length):
            for j in range (4):
                sum_profile_genre[i] += genre_profile_table[j][i]
                sum_profile_years[i] += years_profile_table[j][i]

        # calculate final value
        final_table = np.array((sum_profile_genre*sum_profile_years)/((sum_profile_genre+sum_profile_years)-(sum_profile_genre*sum_profile_years)))
        final_table_temp2 = np.array(final_table)
        
        # sort ascending
        sorted_idx = np.argsort(final_table)

        # reverse sort (asc to desc)
        for i in range (length-1, -1, -1):
            number_temp2[length-1-i] = number[sorted_idx[i]]
            artis_temp2[length-1-i] = artis[sorted_idx[i]]
            lagu_temp2[length-1-i] = lagu[sorted_idx[i]]
            final_table_temp2[length-1-i] = final_table[sorted_idx[i]]
            for j in range(4):
                genre_temp2[j][length-1-i] = genre[j][sorted_idx[i]]
                years_temp2[j][length-1-i] = years[j][sorted_idx[i]]

        # update recomendation
        for i in range (0, length):
            number[i] = number_temp2[i]
            artis[i] = artis_temp2[i]
            lagu[i] = lagu_temp2[i]
            for j in range(4):
                genre[j][i] = genre_temp2[j][i]
                years[j][i] = years_temp2[j][i]
        
        # buat tandain kalau dia bisa balik ke playlist dan ga akan sorting ulang di main
        back_playlist = 1

    # kalau pilih lagu
    if request.method == "POST":
        flag = 1
        user_profile_genre = new_profile_genre
        user_profile_years = new_profile_years
        playing_song = request.form["choose"]
        picked = int(playing_song)
        session["selected_song"] = playing_song
        counter = 1

        for i in range (0, length):
            number_default[i] = number[i]
            artis_default[i] = artis[i]
            lagu_default[i] = lagu[i]
            for j in range(4):
                genre_default[j][i] = genre[j][i]
                years_default[j][i] = years[j][i]
        return redirect(url_for("playlist"))
    else: 
        # kalau lagi dengerin lagu
        if "selected_song" in session:
            title = session["title"]
            singer = session["singer"]
            playing_song = session["selected_song"]
            curr_playing_num = session["curr_playing_num"]
        else: # kalo ga ndengerin lagu
            title = "Nothing"
            singer = "Nothing"
            playing_song = "Nothing"
            curr_playing_num = "Nothing"
        return render_template("main.html",
            page = "MAIN PAGE",
            song_list = zip(number, artis, lagu, final_table_temp2),
            number_show = playing_song,
            singer_show = singer,
            song_show = title,
            profile_genre = user_profile_genre,
            profile_years = user_profile_years,
            curr_song_num = curr_playing_num)

# playlist page
@app.route("/playlist", methods=['GET', 'POST'])
def playlist():
    global flag
    global user_profile_genre
    global user_profile_years
    global new_profile_genre
    global new_profile_years
    global final_table_temp
    global counter
    global picked
    global back_playlist
    global length

    # show what song
    if flag == 1:
        text_number = picked
        int_number = picked
        singer = artis_default[int_number - 1]
        session["singer"] = singer
        song = lagu_default[int_number - 1]
        session["title"] = song
        session["selected_song"] = picked
        curr_playing_num = int(number_default[int_number - 1])
        session["curr_playing_num"] = curr_playing_num
    else:
        text_number = session["selected_song"]
        int_number = int(session["selected_song"])

    # kalau forward/backward
    if request.method == "POST":
        flag = 0
        if request.form["mediabtn"] == "forwardbtn":
            counter+=1
        elif request.form["mediabtn"] == "backwardbtn":
            counter-=1
        text_number = counter
        int_number = counter

    if flag == 0:
        singer = artis_temp[int_number - 1]
        session["singer"] = singer
        song = lagu_temp[int_number - 1]
        session["title"] = song
        session["selected_song"] = counter
        curr_playing_num = int(number_temp[int_number - 1])
        session["curr_playing_num"] = curr_playing_num

    # cuman show sehabis foward/backward
    if flag == 0:
        return render_template("playlist.html",
            number_show = int(text_number)-1,
            singer_show = singer,
            song_show = song,
            song_list = zip(number_temp, artis_temp, lagu_temp, final_table_temp),
            profile_genre = user_profile_genre,
            profile_years = user_profile_years,
            page = "PLAYLIST PAGE",
            showpick = picked,
            song_no = counter,
            curr_song_num = curr_playing_num)

    if flag == 1 or back_playlist == 1:
        back_playlist = 0

        temp_arr_genre = np.array([[0] * 100 for i in range(4)])
        temp_arr_years = np.array([[0] * 100 for i in range(4)])

        total_genre = np.array([[0] * 1 for i in range(4)])
        total_years = np.array([[0] * 1 for i in range(4)])
        cumulative_genre = 0
        cumulative_years = 0

        # assign selected song to temp array
        for i in range (4):
            temp_arr_genre[i][0] = genre_default[i][picked-1]
            total_genre[i][0] += temp_arr_genre[i][0]
            cumulative_genre += temp_arr_genre[i][0]

            temp_arr_years[i][0] = years_default[i][picked-1]
            total_years[i][0] += temp_arr_years[i][0]
            cumulative_years += temp_arr_years[i][0]

        # calculate new profile
        profile_temp_genre = np.array(total_genre/cumulative_genre)
        profile_temp_years = np.array(total_years/cumulative_years)

        new_profile_genre = (user_profile_genre*95/100)+(profile_temp_genre*5/100)
        new_profile_years = (user_profile_years*95/100)+(profile_temp_years*5/100)

        # calculate arr * new profile
        genre_profile_table = np.array(genre*new_profile_genre)
        years_profile_table = np.array(years*new_profile_years)

        # set temp sum array for each song
        sum_profile_genre = np.array([0.0 for x in range(length)])
        sum_profile_years = np.array([0.0 for x in range(length)])

        # sum each song genre/years
        for i in range(length):
            for j in range (4):
                sum_profile_genre[i] += genre_profile_table[j][i]
                sum_profile_years[i] += years_profile_table[j][i]

        # put selected song on top
        number_temp[0] = number_default[picked-1]
        artis_temp[0] = artis_default[picked-1]
        lagu_temp[0] = lagu_default[picked-1]
        for j in range(4):
            genre_temp[j][0] = genre_default[j][picked-1]
            years_temp[j][0] = years_default[j][picked-1]

        # calculate final value
        final_table_default = np.array((sum_profile_genre*sum_profile_years)/((sum_profile_genre+sum_profile_years)-(sum_profile_genre*sum_profile_years)))
        final_table_temp = np.array(final_table_default)

        final_table_temp[0] = final_table_default[picked-1]
        
        # sort ascending
        sorted_idx = np.argsort(final_table_default)

        # reverse sort (asc to desc)
        temp_length = 1
        for i in range (length-1, -1, -1):
            if(sorted_idx[i] == int_number-1):
                continue
            number_temp[temp_length] = number_default[sorted_idx[i]]
            artis_temp[temp_length] = artis_default[sorted_idx[i]]
            lagu_temp[temp_length] = lagu_default[sorted_idx[i]]
            final_table_temp[temp_length] = final_table_default[sorted_idx[i]]
            for j in range(4):
                genre_temp[j][temp_length] = genre_default[j][sorted_idx[i]]
                years_temp[j][temp_length] = years_default[j][sorted_idx[i]]
            temp_length += 1
                
        # update recomendation
        for i in range (0, length):
            number[i] = number_temp[i]
            artis[i] = artis_temp[i]
            lagu[i] = lagu_temp[i]
            for j in range(4):
                genre[j][i] = genre_temp[j][i]
                years[j][i] = years_temp[j][i]

        return render_template("playlist.html",
            number_show = text_number,
            singer_show = singer,
            song_show = song,
            song_list = zip(number, artis, lagu, final_table_temp),
            profile_genre = new_profile_genre,
            profile_years = new_profile_years,
            page = "PLAYLIST PAGE",
            showpick = picked,
            song_no = counter,
            curr_song_num = curr_playing_num)

if __name__ == "__main__":
    app.run(debug = True)
