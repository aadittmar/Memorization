import os

def add_verses_to_dict():

    # Set up Romans 1 Dictionary for all verses
    romans_1_dict[ 1 ] = "Paul, a servant of Christ Jesus, called to be an apostle and set apart for the gospel of God—"
    romans_1_dict[ 2 ] = "the gospel he promised beforehand through his prophets in the Holy Scriptures"
    romans_1_dict[ 3 ] = "regarding his Son, who as to his earthly life[a] was a descendant of David, "
    romans_1_dict[ 4 ] = "and who through the Spirit of holiness was appointed the Son of God in power[b] by his resurrection from the dead: Jesus Christ our Lord."
    romans_1_dict[ 5 ] = "Through him we received grace and apostleship to call all the Gentiles to the obedience that comes from[c] faith for his name’s sake."
    romans_1_dict[ 6 ] = "And you also are among those Gentiles who are called to belong to Jesus Christ."
    romans_1_dict[ 7 ] = "To all in Rome who are loved by God and called to be his holy people: Grace and peace to you from God our Father and from the Lord Jesus Christ."
    romans_1_dict[ 8 ] = "First, I thank my God through Jesus Christ for all of you, because your faith is being reported all over the world."
    romans_1_dict[ 9 ] = "God, whom I serve in my spirit in preaching the gospel of his Son, is my witness how constantly I remember you"
    romans_1_dict[ 10 ] = "in my prayers at all times; and I pray that now at last by God’s will the way may be opened for me to come to you."

    return

def select_verse():

    count = 0 #Count how many times the user has gotten the verse right. Do something after 10 correct times?

    try:
        verse_num = int(input("What verse are you trying to memorize? "))
    except:
        verse_num = "unknown"


    if verse_num in romans_1_dict.keys():
        selected_verse = romans_1_dict[verse_num]
    else:
        print("\nThat is not a valid verse, please try again.\n")
        selected_verse = "unknown"
        select_verse()

    check_answer(selected_verse, count)

    return

def check_answer(selected_verse, count):

    user_answer = input("Print verse: ")

    while user_answer == selected_verse:
        count += 1

        # Try to clear the screen. Only works on windows terminal right now.
        try:
            clear()
        except:    
            pass

        print("Correct ", count, " time")

        # ask the user to enter the verse again if they got it right the previous time.
        user_answer = input("Print again: ")

    else:
        print("\nIncorrect. Correct answer is: ", selected_verse, "\n")
        select_verse()

    return

### START OF PROGRAM ###
print("This is a memorization tool for the NIV 2001 translation of the Bible.\n")

# setup 'clear' command. Only works on Windows right now.
try:
    clear = lambda: os.system('cls')
except:
    pass

romans_1_dict = {}
add_verses_to_dict()

while True:
    select_verse()
