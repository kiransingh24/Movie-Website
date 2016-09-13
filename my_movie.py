import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story",
                        "The Story of a Boy and his Toys that come to life",
                        "https://commons.wikimedia.org/wiki/Category:Toy_Story#/media/File:Toy_Story_logo.svg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
#toy_story.show_trailer()

avatar = movie.Movie("Avatar",
                     "Aliens Story",
                     "https://www.google.com/search?q=avatar+poster+image&rlz=1C1CHBF_enUS703US703&espv=2&biw=1366&bih=643&tbm=isch&imgil=FKv2H8yQwVzueM%253A%253BV9QW9EbsxurAJM%253Bhttp%25253A%25252F%25252Fwww.traileraddict.com%25252Favatar%25252Fposter%25252F1&source=iu&pf=m&fir=FKv2H8yQwVzueM%253A%252CV9QW9EbsxurAJM%252C_&usg=__qh3cFx6cRSsiFzR2J9zc5GD7UUs%3D&ved=0ahUKEwir_qaw7fvOAhUl2IMKHXEwDg8QyjcIQQ&ei=x0vPV-v-EaWwjwTx4Lh4#imgrc=FKv2H8yQwVzueM%3A",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#avatar.show_trailer()

sultan = movie.Movie("Sultan",
                     "A Indian Wrestling Champion's Story",
                     "https://www.google.com/search?q=sultan+poster+image&rlz=1C1CHBF_enUS703US703&espv=2&biw=1366&bih=643&tbm=isch&imgil=GcOELGIx-ucEOM%253A%253BTUxGntzGfTWrIM%253Bhttp%25253A%25252F%25252Fwww.traileraddict.com%25252Fsultan-2016%25252Fposter%25252F1&source=iu&pf=m&fir=GcOELGIx-ucEOM%253A%252CTUxGntzGfTWrIM%252C_&usg=__1pslRYdTigxk_OZtRCdRmgNym98%3D&ved=0ahUKEwjnl8Sk7vvOAhWs7YMKHWRhCB8QyjcINw&ei=u0zPV6fOAqzbjwTkwqH4AQ#imgrc=GcOELGIx-ucEOM%3A",
                     "https://www.youtube.com/watch?v=vU6A1jpe5k8")
#sultan.show_trailer()

Pink = movie.Movie("Pink",
                   "The story of a young girl fighting for Justice",
                   "https://www.google.com/search?q=pink+taapsee+pannu+poster&rlz=1C1CHBF_enUS703US703&espv=2&biw=1366&bih=643&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiDian68fvOAhVB74MKHZR_BCYQ_AUIBigB#imgrc=_JhCEjgt4ZlmPM%3A",
                   "https://www.youtube.com/watch?v=AL2TShb6fFs")
movies = [toy_story, avatar, sultan, Pink]
fresh_tomatoes.open_movies_page(movies)
