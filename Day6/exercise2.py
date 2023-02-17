
# def make_album(name,title):
#     info = {"artist_name":name, "album_title":title}
#     print (info)

# make_album("Andy","drums")
# make_album("James","sky") 
# make_album("Jordan","Street") 

def make_album(artist_name, album_title):
    album = {
        "artist_name":artist_name,
         "album_title": album_title
         }
    return album

album1 = make_album("Andy","drums")
album2 = make_album("James","sky") 
album3 = make_album("Jordan","Street")

print (album1)
print (album2)
print (album3)

