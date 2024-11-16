
# KROK 2
# na základe zvolenej úrovne obtiažnosti nastavte hodnoty
# za životy hráča
word_to_guess = "Cairo"  # vzorové údaje, normálne by sa slovo malo vybrať zo súboru countries-and-capitals.txt
lives = 5  # vzorových údajov, zvyčajne by sa životy mali vyberať na základe náročnosti


# KROK 3
# zobraziť vybrané slovo na uhádnutie so všetkými písmenami nahradenými "_"
# napríklad namiesto "Cairo" zobrazte "_ _ _ _ _"


# KROK 4
# požiadajte používateľa, aby napísal písmeno
# tu by ste mali overiť, či napísané písmeno je slovo
# "QUIT", "Quit", "QUit", "QUIt", "QUIT", "QUIT"... chápeš :)
# TIP: použite vstavané funkcie horného() alebo spodného() Pythonu


# KROK 5
# overte, či je napísané písmeno už v skúšaných písmenách
# TIP: hľadajte na internete: `python, ak je písmeno v zozname`
# Ak nie je, pridajte k osvedčeným písmenám
# Ak už bol napísaný, vráťte sa na KROK 5. TIP: tu použite cyklus while
already_tried_letters = []  # tento zoznam bude obsahovať všetky vyskúšané písmená


# KROK 6
# ak je písmeno prítomné v slove, iterujte cez všetky písmená v premennej
# word_to_guess. Ak sa toto písmeno nachádza v už_vyskúšaných_listoch, zobrazte ho,
# inak zobrazte "_".


# ak sa písmeno v slove nenachádza, znížte hodnotu v premennej životy
# a zobraziť obesenca ASCII art. Na internete môžete vyhľadať výraz „kat ASCII art“,
# alebo si nakreslite nový krásny svojpomocne.


# KROK 7
# skontrolujte, či premenná už_triedené_písmená už obsahuje všetky potrebné písmená
# na vytvorenie hodnoty v premennej word_to_guess. Ak áno, zobrazte výhernú správu a odíďte
# aplikáciu.
# Ak stále máte písmená, ktoré nie sú uhádnuté, skontrolujte, či nemáte záporný počet životov
# zostáva. Ak nie, vytlačte správu o strate a ukončite aplikáciu.
# Ak ani jedna z vyššie uvedených 2 podmienok, vráťte sa ku KROKU 4
# PART 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
difficulty = "1" # sample data, normally the user should choose the difficulty


# STEP 2
# based on the chosen difficulty level, set the values
# for the player's lives
word_to_guess = "Cairo" # sample data, normally the word should be chosen from the countries-and-capitals.txt
lives = 5 # sample data, normally the lives should be chosen based on the difficulty


# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"


# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions


# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
already_tried_letters = [] # this list will contain all the tried letters


# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".


# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.


# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4


# PART 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
difficulty = "1"  # sample data, normally the user should choose the difficulty


# STEP 2
# based on the chosen difficulty level, set the values
# for the player's lives
word_to_guess = "Cairo"  # sample data, normally the word should be chosen from the countries-and-capitals.txt
lives = 5  # sample data, normally the lives should be chosen based on the difficulty


# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"


# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions


# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
already_tried_letters = []  # this list will contain all the tried letters


# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".


# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.


# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4
